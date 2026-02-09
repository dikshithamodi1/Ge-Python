from typing import Optional, List
from fastapi import FastAPI, Query

app = FastAPI()

# Mock database
products_db = [
    {"id": 1, "name": "iPhone 14", "category": "electronics", "price": 999},
    {"id": 2, "name": "Samsung Galaxy S23", "category": "electronics", "price": 899},
    {"id": 3, "name": "Sony Headphones", "category": "electronics", "price": 199},
    {"id": 4, "name": "Leather Wallet", "category": "fashion", "price": 49},
    {"id": 5, "name": "Nike Sneakers", "category": "fashion", "price": 120},
    {"id": 6, "name": "Organic Coffee", "category": "groceries", "price": 15},
    {"id": 7, "name": "MacBook Pro", "category": "electronics", "price": 1999},
    {"id": 8, "name": "LED Desk Lamp", "category": "home", "price": 35},
    {"id": 9, "name": "Yoga Mat", "category": "fitness", "price": 25},
    {"id": 10, "name": "Blender", "category": "home", "price": 60},
    {"id": 11, "name": "Fitbit Charge 5", "category": "fitness", "price": 150},
    {"id": 12, "name": "Dell XPS 13", "category": "electronics", "price": 1200},
]

#ge is greater than,10 is default value checks if user input is greter than or equal to 1
@app.get("/products/search")
def search_products(
    category: Optional[str] = Query(None, description="Filter by category"),
    min_price: Optional[float] = Query(None, description="Minimum price"),
    max_price: Optional[float] = Query(None, description="Maximum price"),
    keyword: Optional[str] = Query(None, description="Search keyword in product name"),
    limit: int = Query(10, ge=1, description="Number of results to return"),
    skip: int = Query(0, ge=0, description="Number of results to skip"),
) -> List[dict]:
    # Start with all products
    results = products_db

    # Apply category filter
    if category:
        results = [p for p in results if p["category"].lower() == category.lower()]

    # Apply minimum price filter
    if min_price is not None:
        results = [p for p in results if p["price"] >= min_price]

    # Apply maximum price filter
    if max_price is not None:
        results = [p for p in results if p["price"] <= max_price]

    # Apply keyword search
    if keyword:
        results = [p for p in results if keyword.lower() in p["name"].lower()]

    # Apply pagination
    results = results[skip : skip + limit]

    return results
