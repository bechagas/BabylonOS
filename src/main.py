from fastapi import FastAPI
from .database.config import Base, engine
from .blog.router import router as blog_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(blog_router)