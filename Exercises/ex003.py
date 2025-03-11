# Your Student ID:  240543022
# Your Name and Surname:  IBRAHIM HALIL SIYLI
from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
current_time=current_datetime.strftime("%H:%M:%S")

print("Current date:", current_datetime.date(),"\nCurrent Time:",current_time, "\nCurrent date and time:", formatted_datetime)
