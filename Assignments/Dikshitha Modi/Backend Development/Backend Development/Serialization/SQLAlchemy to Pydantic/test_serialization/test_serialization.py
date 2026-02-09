def test_orm_serialization():
    db_obj = ProductModel(id=1, name="Widget", price=9.99,
    created_at=now())
    pydantic_obj = ProductDB.from_orm(db_obj)
    assert pydantic_obj.name == "Widget"
    assert pydantic_obj.dict()["price"] == 9.99