from sqlalchemy import (
    Column,
    Date,
    Float,
    Integer,
    LargeBinary,
    SmallInteger,
    String,
    Table,
    Text,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata

class Text(Base):
    __tablename__ = 'texts'

    textID = Column(Integer, primary_key=True, index=True)
    text = Column(String(160), nullable=False)
    counter = Column(Integer)
