import math

def circumference(radius):
    area = math.pi *radius ** 2
    circumference = 2*math.pi*radius
    return area , circumference 

a,c = circumference(3)
print(circumference(2))
print("Area:",a,"Circumference:",c)
