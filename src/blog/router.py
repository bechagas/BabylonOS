from fastapi import APIRouter, status
from ..database.session import db_dependency

router = APIRouter(
    prefix='/api/blog/posts',
    tags=['posts']
)

@router.get('/', status_code=status.HTTP_200_OK)
async def get_posts(db: db_dependency):
    return

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_post(id: int, db: db_dependency):
    return

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_post(db: db_dependency):
    return

@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_all_post(id: int, db: db_dependency):
    return

@router.patch('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_post(id: int, db: db_dependency):
    return

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: db_dependency):
    return
