from datetime import datetime

from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class Dish(Base):
    __tablename__: str = "dishes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    weight: Mapped[float] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), onupdate=text("TIMEZONE('utc', now())")
    )
