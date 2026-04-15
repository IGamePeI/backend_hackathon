from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    COLLECTOR = "collector"

class Status(Enum):
    READY = "ready"
    expected = "expected"

class Category(Enum):
    PAST = "past"
    PRESENT = "present"
    FUTURE = "future"
