# EXAMPLE - 2

# BEFORE REFACTORING:
def check_number(num):
    if num > 0:
        if num % 2 == 0:
            return "Positive Even"
        else:
            return "Positive Odd"
    else:
        if num == 0:
            return "Zero"
        else:
            if num % 2 == 0:
                return "Negative Even"
            else:
                return "Negative Odd"
            
#AFTER REFACTORING:
def check_number(num):
    if num == 0:
        return "Zero"

    sign = "Positive" if num > 0 else "Negative"
    parity = "Even" if num % 2 == 0 else "Odd"

    return f"{sign} {parity}"

