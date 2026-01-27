from datetime import date
date1=date(2014,7,2)
date2=date(2014,7,11)
diff=date2-date1
no_of_days=diff.days
print(f"Date 1:{date1}")
print(f"Date 2:{date2}")
print(f"Difference in days: {no_of_days}")
