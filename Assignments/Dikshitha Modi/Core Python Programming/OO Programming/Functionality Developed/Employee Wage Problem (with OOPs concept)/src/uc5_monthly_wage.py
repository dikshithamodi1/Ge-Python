class MonthlyWage:
    def calculate_monthly_wage(self):
        wage_per_hour = 20
        full_day_hours = 8
        working_days = 20

        monthly_wage = wage_per_hour * full_day_hours * working_days
        print("Monthly Employee Wage:", monthly_wage)

        return monthly_wage


if __name__ == "__main__":
    monthly = MonthlyWage()
    monthly.calculate_monthly_wage()
