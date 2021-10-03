from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import init_db, get_session
from app.models import Product, Offer, History

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/history", response_model=List[History])
async def get_history(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(History))
    return result.scalars().all()


@app.get("/products", response_model=List[Product])
async def get_products(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product))
    return result.scalars().all()


@app.post("/product")
async def add_product(product: Product, session: AsyncSession = Depends(get_session)):
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


@app.post("/offer")
async def add_offer(offer: Offer, session: AsyncSession = Depends(get_session)):
    session.add(offer)
    await session.commit()
    await session.refresh(offer)
    return offer
