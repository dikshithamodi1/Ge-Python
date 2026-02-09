import random

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

        print("Total Days Worked:", total_days)
        print("Total Hours Worked:", total_hours)
        print("Total Wage:", total_wage)

        return total_wage


if __name__ == "__main__":
    condition = ConditionalWage()
    condition.calculate_wage_with_condition()
