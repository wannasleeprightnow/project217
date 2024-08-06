from abc import ABC, abstractmethod
from typing import Generic, Optional, Sequence, Type, TypeVar
from uuid import UUID

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

ModelT = TypeVar("ModelT")


class AbstractRepository(ABC, Generic[ModelT]):

    def __init__(self, session: AsyncSession):
        self.session = session

    @abstractmethod
    async def insert_one(self, **data: dict) -> ModelT:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> Sequence[ModelT]:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository[ModelT]):
    model: Type[ModelT]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert_one(self, **data: dict) -> ModelT:
        stmt = insert(self.model).values(**data).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def get_all(self) -> Sequence[ModelT]:
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_one(self, **filter_by: dict) -> Optional[ModelT]:
        stmt = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_one(
        self,
        item_id: UUID,
        **data: dict,
    ) -> Optional[ModelT]:
        stmt = (
            update(self.model)
            .values(data)
            .filter_by(id=item_id)
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def delete_one_by_id(self, item_id: UUID) -> Optional[ModelT]:
        stmt = delete(self.model).filter_by(id=item_id).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
