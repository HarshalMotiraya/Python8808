input_age = input("Enter your age: ")
age = int(input_age)
day = "Wednesday"

price = 12 if age <=18 else 8

if day ==  "wednesday":
    price = price - 2

print("ticket price for yiu $ :",price)