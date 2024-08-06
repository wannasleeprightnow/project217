from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from settings import settings

engine = create_async_engine(settings.postgres_dsn, echo=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):

    def __repr__(self) -> str:
        cols: list[str] = [
            f"{col}={getattr(self, col)}"
            for col in self.__table__.columns.keys()
        ]
        return " ".join(cols)
