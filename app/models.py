from sqlalchemy import Column, Integer, String
from app.database import Base

class Text(Base):
    __tablename__ = 'texts'

    textID = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    counter = Column(Integer)