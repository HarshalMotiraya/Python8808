# problem - Write a Python program to check if a given year is a leap year or not. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.Here is a Python program that checks if a given year is a leap year or not:


year = 2022

if  (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0) :
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")