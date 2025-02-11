#1.
from datetime import datetime, timedelta

current_date = datetime.today()
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date after subtracting 5 days:", new_date.strftime("%Y-%m-%d"))


#2.
from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))


#3.
from datetime import datetime

current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", datetime_without_microseconds)


#4.
from datetime import datetime

date1 = datetime(2024, 2, 1, 12, 30, 0)  #мойпример
date2 = datetime(2024, 2, 10, 14, 45, 30)  #мойпример

difference = abs((date2 - date1).total_seconds())

print(f"Difference in seconds: {difference}")

