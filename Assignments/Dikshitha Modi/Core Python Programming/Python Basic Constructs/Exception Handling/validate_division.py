def divide_sales(num, den):
    try:
        ans=num/den
    except ZeroDivisionError:
        return 0
    else:
        print(f"Success : {ans}")
    finally:
        print("Log Closed")
divide_sales(100, 20) 
