from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    content: str = Field(min_length=1)

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    # user_id: int
    date_posted: datetime
    # author: UserResponse