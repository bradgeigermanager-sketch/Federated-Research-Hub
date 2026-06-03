class Title(Base):
    __tablename__ = 'title'
    id = Column(String, primary_key=True)
    title = Column(String)
    # Track which plugin provided this data for auditability
    origin_plugin = Column(String)
