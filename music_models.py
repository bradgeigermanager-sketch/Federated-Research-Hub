from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

contribution = Table('contribution', Base.metadata,
    Column('title_id', String, ForeignKey('title.id')),
    Column('person_id', String, ForeignKey('person.id')),
    Column('role', String)
)

class Title(Base):
    __tablename__ = 'title'
    id = Column(String, primary_key=True)
    title = Column(String)
    origin_plugin = Column(String) # Audit trail

class Album(Base):
    __tablename__ = 'album'
    id = Column(String, primary_key=True)
    title = Column(String)
    label_id = Column(String, ForeignKey('label.id'))
