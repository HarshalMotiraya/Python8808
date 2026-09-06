#Fruit Ripeness Checker
# problem : Determine if a fruit is ripe , overripe , or unripe based its color (e.g , Banana :Green -Unripe , Yellow - Ripe , Brown -Overripe)

fruit =  "Banana"
Color = "Yellow"

if fruit == "Banana":
    if Color == "Green":
        print("the banana is unripe")
    elif Color == "Yellow":
        print("the banana is ripe")
    elif Color == "Brown":
        print("the banana is overripe")
    else : 
        print("the banana is not in the list")
