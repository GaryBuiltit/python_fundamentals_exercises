
from calendar import THURSDAY


inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(snowInches):
    totalInches = 0
    for day, inches in snowInches.items():
        totalInches += inches
    print(f"Total snowfall inches: {totalInches}")


print_total_snowfall(inches_snow)
inches_snow["Thursday"] = int(
    input("How many inches of snow fell on Thursday? "))

print_total_snowfall(inches_snow)
