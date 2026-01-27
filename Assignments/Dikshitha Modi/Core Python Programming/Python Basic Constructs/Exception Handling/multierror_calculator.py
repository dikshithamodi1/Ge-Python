ef smart_calculate(a_str, b_str) :
    try:
        a=int(a_str)
        b=int(b_str)
        result=a/b
        print(result)
    except ValueError:
        print("invalid number")
    except ZeroDivisionError:
        print("Can't divide by zero")
smart_calculate("10", "0")
