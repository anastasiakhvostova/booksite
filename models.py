import datetime
from fastapi import FastAPI, Depends, HTTPException, status
from tortoise.contrib.fastapi import register_tortoise
from tortoise import fields
from tortoise.models import Model
from tortoise.transactions import in_transaction
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, Float, String, DateTime, Boolean,
    ForeignKey,
)
from sqlalchemy.orm import Mapper, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

from database import Base


class BaseInfoMixin:
    id = Column(Integer, primary_key=True)
    # id: Mapper[int] = mapped_column(primary_key=True)
    notes = Column(String(200))
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)


class User(BaseInfoMixin, Base):
    __tablename__ = 'user'

    name = Column(String, nullable=False)
    login = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_conflict = Column(Boolean, default=False)
    # notes = relationship("Note", back_populates="owner")

    def __repr__(self) -> str:
        return f'User {self.name} -> #{self.id}'


class Order(BaseInfoMixin, Base):
    __tablename__ = 'order'

    book_quantity = Column(Integer, nullable=False)
    book_price = Column(Float, nullable=False)
    customer = Column(ForeignKey('user.id'))
    new_column = Column('book.id')

    # customer: Mapper[int] = mapped_column(ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'Order #{self.id}'


class Comment(BaseInfoMixin, Base):
    __tablename__ = 'comment'
    comment = Column(String(1000))
