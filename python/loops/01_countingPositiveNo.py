# pronblem = given a list of numbers, write a python program to count the number of positive numbers in the list.
# number = I[ 1,-2,3,-4,5,6,-7,8,9,10]

number = [ 1,-2,3,-4,5,6,-7,8,9,10]

positive_number_count = 0 

for num in number:
    if num > 0:
        positive_number_count += 1
print("final count of positive numeber is :",positive_number_count)