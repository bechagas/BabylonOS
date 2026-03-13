from fastapi import APIRouter, Depends, status
from typing import Annotated

from .schemas import PostCreate, PostUpdate, PostResponse
from .services import get_post_service, PostService

router = APIRouter(
    prefix='/api/blog/posts',
    tags=['Posts']
)

service_dependency = Annotated[PostService, Depends(get_post_service)]

@router.get('/', response_model=list[PostResponse], status_code=status.HTTP_200_OK)
async def get_posts(service: service_dependency):
    return await service.get_all_posts()

@router.get('/{post_id}', response_model=PostResponse, status_code=status.HTTP_200_OK)
async def get_post(post_id: int, service: service_dependency):
    return await service.get_post_by_id(post_id)


@router.post('/', response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, service: service_dependency):
    return await service.create_new_post(post)

@router.put('/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_all_post(post_id: int, post: PostCreate, service: service_dependency):
    await service.update_post_full(post_id, post)

@router.patch('/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_post(post_id: int, post: PostUpdate, service: service_dependency):
    await service.update_post_partial(post_id, post)

@router.delete('/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, service: service_dependency):
    await service.delete_post(post_id)