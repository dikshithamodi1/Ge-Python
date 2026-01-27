def category_wise_sales(sales_data):
    totals={}
    for key,val in sales_data:
        if key in totals:
            totals[key]+=val
        else:
            totals[key]=val
    print(totals) 
sales_data=[("Electronics", 1000), ("Furniture", 2000), ("Electronics", 1500)]
category_wise_sales(sales_data)
