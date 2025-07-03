# Imports
from pydantic import BaseModel, ConfigDict


# Post models
class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    model_config = ConfigDict(from_attributes=True)
    id: int


# Comment Models
class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    model_config = ConfigDict(from_attributes=True)
    id: int


# Composite model
class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]
