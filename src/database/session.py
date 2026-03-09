from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from .config import SessionLocal

def get_db():
    with SessionLocal() as db:
        yield db

db_dependency = Annotated[Session, Depends(get_db)]