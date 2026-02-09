from sqlalchemy.dialects.postgresql import JSONB, ARRAY

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    meta_data = Column(JSONB)  # Stores arbitrary JSON
    tags = Column(ARRAY(String))  # Stores array of strings


# Querying JSONB
@app.get("/docs/search")
def search_docs(key: str, value: str, db: Session = Depends(get_db)):
    # Find docs where meta_data->key equals value
    return db.query(Document).filter(
        Document.meta_data[key].astext == value
    ).all()