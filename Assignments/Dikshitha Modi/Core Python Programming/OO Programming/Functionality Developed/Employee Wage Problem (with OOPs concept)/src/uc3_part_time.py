class PartTimeWage:
    def calculate_part_time_wage(self):
        wage_per_hour = 20
        part_time_hours = 4

        part_time_wage = wage_per_hour * part_time_hours
        print("Part Time Employee Wage:", part_time_wage)

        return part_time_wage


if __name__ == "__main__":
    part_time = PartTimeWage()
    part_time.calculate_part_time_wage()
