from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# User model for storing user data  
class User(BaseModel):
    user_id: Optional[int] = Field(None,alias="id")
    username: str
    email: str
    password: str
    role: str ="user"
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True

# Page model for storing user pages
class LinkedInPage(BaseModel):
    page_id: Optional[int] = Field(None,alias="id")
    user_id: int
    page_name: str
    page_url: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True

# Post model for storing user posts 
class LinkedInPost(BaseModel):
    post_id: Optional[int] = Field(None,alias="id")
    page_id: int
    post_content: str
    post_url: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True

# Comment model for storing post comments
class Comment(BaseModel):
    comment_id: Optional[int] = Field(None,alias="id")
    post_id: int
    user_id: int
    comment_content: str
    commented_at: datetime = Field(default_factory=datetime.now)
    likes_count: int = 0
    liked_by: List[int] = []
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True

# Metrics model for storing post metrics data 
class Metrics(BaseModel):
    metric_id: Optional[int] = Field(None,alias="id")
    post_id: int
    likes_count: int = 0
    comments_count: int = 0
    views_count: int = 0
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True

# Suggestions model for storing user suggestions    
class Suggestions(BaseModel):
    suggestion_id: Optional[int] = Field(None,alias="id")
    user_id: int
    suggested_contennt: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True

# History model for storing user actions
class History(BaseModel):
    history_id: Optional[int] = Field(None,alias="id")
    user_id: int
    post_id: int
    action: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True

# Trend model for storing trends data
class Trend(BaseModel):
    trend_id: Optional[int] = Field(None,alias="id")
    user_id: int
    trend_type: str
    trend_value: str
    generated_at: datetime = Field(default_factory=datetime.now)
    Valid_till: Optional[datetime] = None

    class Config:
        orm_mode = True