from fastapi import APIRouter, Depends
from app.db import comments_collection,posts_collection

router = APIRouter(prefix="/comments", tags=["comments"])

@router.get("/")
def add_comment(post_id:int,comment:str):
    pass