# leap_year_checker.py
# A simple program to check if a year is a leap year or not.

print("📅 Leap Year Checker")

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year ✅")
else:
    print(f"{year} is not a leap year ❌")
