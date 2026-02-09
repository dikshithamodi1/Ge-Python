def test_jsonb_query(db_session):
    doc = Document(meta_data={"author": "dave", "pages": 10})
    db_session.add(doc)
    db_session.commit()

    results = db_session.query(Document).filter(
        Document.meta_data["author"].astext == "dave"
    ).all()

    assert len(results) == 1