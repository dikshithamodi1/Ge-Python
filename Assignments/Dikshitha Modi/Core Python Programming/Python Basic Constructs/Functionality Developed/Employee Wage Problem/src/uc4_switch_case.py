def calculate_wage_by_type(employee_type):
    wage_per_hour = 20

    if employee_type == 1:
        hours = 8
        print("Full Time Employee")
    elif employee_type == 2:
        hours = 4
        print("Part Time Employee")
    else:
        hours = 0
        print("Employee Absent")

    wage = wage_per_hour * hours
    print("Calculated Wage:", wage)

    return wage
