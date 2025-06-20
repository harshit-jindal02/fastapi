from sqlalchemy import Column, Integer, Text, Boolean
from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    done = Column(Boolean, default=False)
