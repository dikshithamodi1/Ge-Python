# Response models module
from pydantic import BaseModel

class Overview(BaseModel):
    total_stores:int
    total_weeks:int
    avg_weekly_sales:float
    holiday_sales_lift_percent:float
