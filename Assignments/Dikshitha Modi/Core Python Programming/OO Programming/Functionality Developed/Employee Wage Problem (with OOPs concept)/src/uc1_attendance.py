import random

class Attendance:
    def check_attendance(self):
        is_present = random.randint(0, 1)

        if is_present == 1:
            print("Employee is Present")
        else:
            print("Employee is Absent")

        return is_present


if __name__ == "__main__":
    attendance = Attendance()
    attendance.check_attendance()
