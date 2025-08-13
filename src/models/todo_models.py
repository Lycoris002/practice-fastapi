from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id: Column = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    title: Column = Column(String, nullable=False)
    completed: Column = Column(Boolean, default=False)
    created_at: Column = Column(DateTime, default=datetime.now)
    updated_at: Column = Column(DateTime, default=datetime.now, onupdate=datetime.now)