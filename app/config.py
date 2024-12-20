import os
class Config:
    """
    Configuration class for LinkedIn automation tool.
    """
    
    LINKEDIN_API_URL = os.getenv('LINKEDIN_API_URL', 'https://api.linkedin.com/v2/')
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://vrajclerk04:vrajclerk04@linkedin.kr6rq.mongodb.net/?retryWrites=true&w=majority&appName=linkedIn')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'linkedin_automation')