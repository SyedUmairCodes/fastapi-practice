# Imports
from fastapi import APIRouter, HTTPException

from storeapi.models.post import (
    Comment,
    CommentIn,
    UserPost,
    UserPostIn,
    UserPostWithComments,
)

# Router object
router = APIRouter()
# Using dictionaries as temporary DB
post_table = {}
comment_table = {}


# Method to find posts with their IDs
def find_post(post_id: int):
    return post_table.get(post_id)


# POST route for posts
@router.post("/post", response_model=UserPost, status_code=201)
async def create_post(post: UserPostIn):
    data = post.model_dump()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post


# GET route for posts
@router.get("/post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())


# POST route for comments
@router.post("/comment", response_model=Comment, status_code=201)
async def create_comment(comment: CommentIn):
    post = find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    data = comment.model_dump()
    last_record_id = len(comment_table)
    new_comment = {**data, "id": last_record_id}
    comment_table[last_record_id] = new_comment
    return new_comment


# GET route for comments
@router.get("/post/{post_id}/comment", response_model=list[Comment])
async def get_comments_on_posts(post_id: int):
    return [
        comment for comment in comment_table.values() if comment["post_id"] == post_id
    ]


# GET route for getting posts with comments
@router.get("/post/{post_id}", response_model=UserPostWithComments)
async def get_post_with_comments(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"post": post, "comments": await get_comments_on_posts(post_id)}
