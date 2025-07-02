# Imports
from pydantic import BaseModel


# Post models
class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int


# Comment Models
class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    id: int


# Composite model
class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]
