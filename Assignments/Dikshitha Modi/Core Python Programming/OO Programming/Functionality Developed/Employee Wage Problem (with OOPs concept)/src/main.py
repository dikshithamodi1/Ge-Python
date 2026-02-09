import random

print("Welcome to Employee Wage Computation Program")

# UC 1 – Attendance Check
class Attendance:
    def check_attendance(self):
        is_present = random.randint(0, 1)

        if is_present == 1:
            print("UC1: Employee is Present")
        else:
            print("UC1: Employee is Absent")

        return is_present


# UC 2 – Daily Wage
class DailyWage:
    def calculate_daily_wage(self):
        wage_per_hour = 20
        full_day_hours = 8

        daily_wage = wage_per_hour * full_day_hours
        print("UC2: Daily Employee Wage:", daily_wage)

        return daily_wage


# UC 3 – Part Time Wage
class PartTimeWage:
    def calculate_part_time_wage(self):
        wage_per_hour = 20
        part_time_hours = 4

        part_time_wage = wage_per_hour * part_time_hours
        print("UC3: Part Time Employee Wage:", part_time_wage)

        return part_time_wage


# UC 4 – Switch Case
class WageByType:
    def calculate_wage(self, employee_type):
        wage_per_hour = 20

        if employee_type == 1:
            hours = 8
            print("UC4: Full Time Employee")
        elif employee_type == 2:
            hours = 4
            print("UC4: Part Time Employee")
        else:
            hours = 0
            print("UC4: Employee Absent")

        wage = wage_per_hour * hours
        print("UC4: Calculated Wage:", wage)

        return wage


# UC 5 – Monthly Wage
class MonthlyWage:
    def calculate_monthly_wage(self):
        wage_per_hour = 20
        full_day_hours = 8
        working_days = 20

        monthly_wage = wage_per_hour * full_day_hours * working_days
        print("UC5: Monthly Employee Wage:", monthly_wage)

        return monthly_wage


# UC 6 – Wage Till Condition
class ConditionalWage:
    def calculate_wage_with_condition(self):
        wage_per_hour = 20
        max_hours = 100
        max_days = 20

        total_hours = 0
        total_days = 0

        while total_hours < max_hours and total_days < max_days:
            total_days += 1
            employee_type = random.randint(0, 2)

            if employee_type == 1:
                hours = 8
            elif employee_type == 2:
                hours = 4
            else:
                hours = 0

            total_hours += hours

        total_wage = total_hours * wage_per_hour

        print("UC6: Total Days Worked:", total_days)
        print("UC6: Total Hours Worked:", total_hours)
        print("UC6: Total Wage:", total_wage)

        return total_wage


# RUN UCs ONE BY ONE
if __name__ == "__main__":

    attendance = Attendance()
    is_present = attendance.check_attendance()

    if is_present:
        DailyWage().calculate_daily_wage()
        PartTimeWage().calculate_part_time_wage()
        WageByType().calculate_wage(1)
        MonthlyWage().calculate_monthly_wage()
        ConditionalWage().calculate_wage_with_condition()