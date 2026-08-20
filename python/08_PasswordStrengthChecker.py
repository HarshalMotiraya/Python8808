
password = input("Enter Your Password: ")

has_length = len(password) >= 8
has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper  = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

score = 0

if has_length:
    score += 1
if has_upper:
    score += 1
if has_lower:   
    score += 1
if has_digit:
    score += 1

print("\n -- Password Strength Checker --")


if score == 4:
    print("Your password is strong.")
elif score == 3:
    print("Your password is moderate.")
else:
    print("Your password is weak.") 


print("\n --Password Suggestion to Improvement")

if not has_length:
    print("Your password should be at least 8 characters long.")
if not has_upper:
    print("Your password should contain at least one uppercase letter.")    
if not has_digit:
    print("Your password should contain at least one digit.")