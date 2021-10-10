from typing import List
from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db import init_db, get_session
from app.models import Product, Offer, History
from app.updater import Updater
from app.utils import start_timestamp

app = FastAPI()

app.mount("/admin", StaticFiles(directory="static", html=True), name="static")

# @app.on_event("startup")
# async def on_startup():
#     await init_db()


@app.get("/")
async def redirect_typer():
    return RedirectResponse("/admin/", status_code=302)


@app.get("/products", response_model=List[Product])
async def get_products(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product).order_by("name"))
    return result.scalars().all()


@app.post("/product", response_model=Product)
async def add_product(product: Product, session: AsyncSession = Depends(get_session)):
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


@app.post("/offer", response_model=Offer)
async def add_offer(offer: Offer, session: AsyncSession = Depends(get_session)):
    session.add(offer)
    await session.commit()
    await session.refresh(offer)
    return offer


@app.get("/update")
async def start_update(session: AsyncSession = Depends(get_session)):
    upd = Updater(session)
    result = await upd.update_all()
    await session.commit()
    return result


@app.get("/history", response_model=List[History])
async def get_history(
    product: int = 0, period: str = "all", session: AsyncSession = Depends(get_session)
):
    result = await session.execute(
        select(History)
        .join(Offer)
        .where(Offer.product_id == product if product else True)
        .where(History.datetime > start_timestamp(period))
        .order_by(History.datetime)
    )
    return result.scalars().all()
