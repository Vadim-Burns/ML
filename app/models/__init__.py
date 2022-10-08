from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):
    ...


class ArticleModel(Base):
    title: str
    text: str
    publish_date: datetime
