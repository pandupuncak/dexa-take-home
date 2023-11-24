from sqlalchemy import CHAR, Column, BigInteger, String, Text
from .database import Base

class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(CHAR(20))
    description = Column(String(255))
    status = Column(Text)
