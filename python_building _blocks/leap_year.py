# Check if user given year is a leap year

input_leapyear = int(input("Enter a year :"))

if input_leapyear % 4 == 0 and input_year % 100 == 0:
    print(f"{input_leapyear} is a leap year")