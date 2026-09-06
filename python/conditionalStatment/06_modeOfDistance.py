
distance = 100

if distance < 3:
    mode = "walk"
elif distance < 8:
    mdoe = "bike"
elif distance <15:
    mode = "car"
else:
    mode = "bus"

print("mdoe of distance cover using is :",mode )
