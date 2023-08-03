from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pathlib import Path


class Settings(BaseSettings):
    DB_URL: str = 'postgresql+asyncpg://isac14fer:post1408@localhost:5432/startup'
    DBBaseModel = declarative_base()
    TEMPLATES = Jinja2Templates(directory='templates')
    MEDIA = Path('media')
    AUTH_COOKIE_NAME: str = 'guniversity'
    SALTY: str = '7xsIchuzya2gcszhxCY181sT7vaJ_JkCjh6xqxRkpfqfGWI1se6VtKThigQQOjCrWYs1MnIfwOtANlgacfxgLg'

    class Config:
        case_sensitive = True

settings: Settings = Settings()
