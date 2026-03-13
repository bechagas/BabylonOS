from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from .config import AsyncSessionLocal

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

db_dependency = Annotated[AsyncSession, Depends(get_db)]