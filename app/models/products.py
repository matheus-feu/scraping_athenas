import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.db.base_model import Base


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    link = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    reviews = Column(String(255), nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
