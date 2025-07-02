from .session import engine
from ..db.base import Base
from ..models import *  # noqa


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
