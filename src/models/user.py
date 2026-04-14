from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import Enum, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db import Base
from utils.enums import UserRole

if TYPE_CHECKING:
    from .order import Order


class User(Base):
    __tablename__: str = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), onupdate=text("TIMEZONE('utc', now())")
    )
    orders: Mapped[List["Order"]] = relationship(back_populates="user", cascade="all, delete-orphan")
