from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import Enum, ForeignKey, text
from sqlalchemy.dialects.postgresql import ARRAY, INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db import Base
from utils.enums import Status

if TYPE_CHECKING:
    from .user import User


class Order(Base):
    __tablename__: str = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    dishes_id: Mapped[List[int]] = mapped_column(ARRAY(INTEGER))
    address: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(Enum(Status), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), onupdate=text("TIMEZONE('utc', now())")
    )

    user: Mapped["User"] = relationship(back_populates="orders")
