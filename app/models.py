from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category: str
    name: str
    image: Optional[str] = None
    description: Optional[str] = None
    offers: Optional[List["Offer"]] = Relationship(back_populates="product")


class Offer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(default=None, foreign_key="product.id")
    check_interval: int = Field(default=24 * 60 * 60)
    url: str
    product: Product = Relationship(back_populates="offers")
    history: Optional[List["History"]] = Relationship(back_populates="offer")


class History(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    offer_id: int = Field(default=None, foreign_key="offer.id")
    datetime: int
    availability: int
    price: int
    price_currency: str
    offer: Offer = Relationship(back_populates="history")
