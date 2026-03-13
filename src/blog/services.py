from fastapi import HTTPException, status

from .repository import PostRepository
from .schemas import PostCreate, PostUpdate
from ..database.session import db_dependency

class PostService():
    def __init__(self, repository: PostRepository):
        self.repository = repository

    async def get_all_posts(self):
        return await self.repository.get_all()
    
    async def get_post_by_id(self, post_id: int):
        post = await self.repository.get_by_id(post_id)
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found!"
            )
        return post
    
    async def create_new_post(self, post: PostCreate):
        return await self.repository.create(post)
    
    async def update_post_full(self, post_id: int, post: PostCreate):
        post = await self.get_post_by_id(post_id)
        update_data = post.model_dump()
        return await self.repository.update(post, update_data)

    async def update_post_partial(self, post_id: int, post: PostUpdate):
        post = await self.get_post_by_id(post_id)
        update_data = post.model_dump(exclude_unset=True)
        return await self.repository.update(post, update_data)
    
    async def delete_post(self, post_id: int):
        post = await self.get_post_by_id(post_id)
        await self.repository.delete(post)

async def get_post_service(db: db_dependency) -> PostService:
    repository = PostRepository(db)
    return PostService(repository)