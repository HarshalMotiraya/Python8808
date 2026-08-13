
age = input(" Provide your age: ")
age_in_int = int(age)

if age_in_int < 18:
    print("You are a minor.")
elif age_in_int >= 20 and age_in_int < 60:
    print("Teenager")

elif age_in_int < 60:
    print("you are adult")

else:
    print("else")

