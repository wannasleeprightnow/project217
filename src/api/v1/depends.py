from typing import Annotated

from fastapi import Depends

from utils.unitofwork import AbstractUnitOfWork, UnitOfWork


UoWdepend = Annotated[AbstractUnitOfWork, Depends(UnitOfWork)]
