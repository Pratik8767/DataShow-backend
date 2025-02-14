# from pydantic import BaseModel
# from sqlalchemy import  Column, Integer, String, Boolean, MetaData, DateTime, text, ForeignKey,Float

# from db_session import Base
# class FileTable(Base):
#     __tablename__ = "files"
#     __table_args__ = {'schema': "public"}
#     id = Column("id",String, primary_key=True, index=True)
#     file_name = Column(String)
#     uploaded_at = Column(DateTime(timezone=True), server_default=text("(now() at time zone 'utc')"))
#     row_count = Column(Integer)
#     column_count = Column(Integer)
#     empty_cells = Column(Integer) 

from sqlalchemy import Column, Integer, String, DateTime, text
from db_session import Base

class FileTable(Base):
    __tablename__ = "files"
    __table_args__ = {'schema': "public"}

    id = Column(String, primary_key=True, index=True)
    file_name = Column(String)
    uploaded_at = Column(DateTime(timezone=True), server_default=text("(now() at time zone 'utc')"))
    row_count = Column(Integer)
    column_count = Column(Integer)
    empty_cells = Column(Integer)
