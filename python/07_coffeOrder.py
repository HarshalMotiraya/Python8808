
cofferOrder = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

if cofferOrder == "espresso":
    print("You have ordered an espresso.")
elif cofferOrder == "latte":
    print("You have ordered a latte.")
elif cofferOrder == "cappuccino":   
    print("You have ordered a cappuccino.")
else:
    print("Sorry, we don't have that option.")

print("Thank you for your order!")