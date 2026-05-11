from pydantic import BaseModel
from typing import Optional


class NewsArticle(BaseModel):
    title: Optional[str]
    publisher: Optional[str]
    link: Optional[str]