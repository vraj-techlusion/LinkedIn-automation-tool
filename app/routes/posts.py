from fastapi import APIRouter, Depends

router = APIRouter(prefix="/posts", tags=["posts"])

@router.get("/")
def fetch_posts(page_id:int):
    pass