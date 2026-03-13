from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .model import Post
from .schemas import PostCreate

class PostRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        query = select(Post)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, post_id: int):
        query = select(Post).where(Post.id == post_id)
        result = await self.db.execute(query)
        return result.scalars().first()

    async def create(self, post: PostCreate) -> Post:
        new_post = Post(**post.model_dump())
        self.db.add(new_post)
        await self.db.commit()
        await self.db.refresh(new_post)
        return new_post

    async def update(self, post: Post, update_data: dict) -> Post:
        for field, value in update_data.items():
            setattr(post, field, value)
        await self.db.commit()
        await self.db.refresh(post)
        return post

    async def delete(self, post: Post):
        await self.db.delete(post)
        await self.db.commit()