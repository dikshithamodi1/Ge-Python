print("Welcome to Employee Wage Computation Program")

from uc1_attendance import check_attendance
from uc2_daily_wage import calculate_daily_wage
from uc3_part_time import calculate_part_time_wage
from uc4_switch_case import calculate_wage_by_type
from uc5_monthly_wage import calculate_monthly_wage
from uc6_condition_wage import calculate_wage_with_conditions

if check_attendance():
    calculate_daily_wage()
    calculate_part_time_wage()
    calculate_wage_by_type(1)   # 1 = Full Time
    calculate_monthly_wage()
    calculate_wage_with_conditions()
