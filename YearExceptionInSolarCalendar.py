import turtle

try:
    year = int(input("Please enter a year based on Garegorian Calender: "))

    leap_or = year % 4 == 0
    if leap_or:
        print("This year is Kabise")
    else:
        print("This year is a ordinary year")
except ValueError:
    print("Only digits are allowed!")
