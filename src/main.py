from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database.config import Base, engine
from .blog.router import router as blog_router

@asynccontextmanager
async def lifespan(_app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.include_router(blog_router)