from fastapi import APIRouter, HTTPException, status
from ..database.session import db_dependency

from .model import Post
from .schemas import PostCreate, PostUpdate, PostResponse

router = APIRouter(
    prefix='/api/blog/posts',
    tags=['posts']
)

@router.get('/', response_model=list[PostResponse], status_code=status.HTTP_200_OK)
async def get_posts(db: db_dependency):
    return db.query(Post).all()

@router.get('/{id}', response_model=PostResponse, status_code=status.HTTP_200_OK)
async def get_post(id: int, db: db_dependency):
    db_post = db.query(Post).filter(Post.id == id).first()

    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found!"
        )
    
    return db_post

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_post(db: db_dependency, post: PostCreate):
    new_post = Post(
        title=post.title,
        content=post.content
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_all_post(id: int, db: db_dependency, post: PostCreate):
    db_post = db.query(Post).filter(Post.id == id).first()

    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found!"
        )
    
    db_post.title = post.title
    db_post.content = post.content

    db.commit()

@router.patch('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_post(id: int, db: db_dependency, post: PostUpdate):
    db_post = db.query(Post).filter(Post.id == id).first()

    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found!"
        )

    update_post = post.model_dump(exclude_unset=True)

    for key, value in update_post.items():
        setattr(db_post, key, value)

    db.commit()

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: db_dependency):
    db_post = db.query(Post).filter(Post.id == id).first()

    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found!"
        )
    
    db.delete(db_post)
    db.commit()