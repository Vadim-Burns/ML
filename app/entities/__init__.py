"""Object for database"""
import datetime
import uuid

from sqlalchemy import Column, DateTime, Text, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.sql import func

Base: DeclarativeMeta = declarative_base()


class BaseEntity(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.now())

    def dict(self) -> dict:
        return self.__dict__


class ArticleEntity(BaseEntity):
    __tablename__ = "articles"

    title = Column(String)
    text = Column(Text)
    publish_date = Column(DateTime(timezone=True))
    link = Column(String)
    role = Column(String)


class ScoreEntity(BaseEntity):
    __tablename__ = "scores"

    okved = Column(String)
    role = Column(String)
    oborot = Column(String)
    score = Column(Float)

    article = Column(UUID(as_uuid=True), ForeignKey('articles.id', ondelete='CASCADE'),
                     nullable=False)
