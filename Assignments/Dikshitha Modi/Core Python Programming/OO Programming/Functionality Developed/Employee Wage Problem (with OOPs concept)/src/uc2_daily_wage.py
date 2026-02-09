class DailyWage:
    def calculate_daily_wage(self):
        wage_per_hour = 20
        full_day_hours = 8

        daily_wage = wage_per_hour * full_day_hours
        print("Daily Employee Wage:", daily_wage)

        return daily_wage


if __name__ == "__main__":
    daily = DailyWage()
    daily.calculate_daily_wage()
