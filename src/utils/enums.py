from enum import Enum


class UserRole(Enum):
    USER = "user"
    ADMIN = "admin"
    DELIVERY_MAN = "delivery_man"
    COLLECTOR = "collector"

class Status(Enum):
    READY = "ready"
    expected = "expected"
