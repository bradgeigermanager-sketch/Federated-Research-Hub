```python
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
    origin_plugin = Column(String)

class Person(Base):
    __tablename__ = 'person'
    id = Column(String, primary_key=True)
    name = Column(String)
    works = relationship("Title", secondary=contribution)

```
