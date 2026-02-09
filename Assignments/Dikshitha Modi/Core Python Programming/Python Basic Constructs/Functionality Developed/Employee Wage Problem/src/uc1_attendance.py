import random

def check_attendance():
    # 0 = Absent, 1 = Present
    attendance = random.randint(0, 1)

    if attendance == 1:
        print("Employee is Present")
        return True
    else:
        print("Employee is Absent")
        return False
