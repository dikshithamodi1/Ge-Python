class ProductBase(BaseModel):
    name: str
    price: float
class ProductDB(ProductBase):
    id: int
    created_at: datetime
class Config:
    orm_mode = True