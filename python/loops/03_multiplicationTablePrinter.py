# Multiplication Table Printer
# problem : Print the multiplication table of a given number up to 10 ,  but skip the fifth iteration  .

# number = 3

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(number , 'multiplied by' , i , "=" , number * i)


# # 3 X 1 = 3
# 3 X 2 = 6
# 3 X 3 = 9


number = int(input("Enter a number to print its multiplication table: "))
for i in range(1,11):
    print(number , 'X' , i , "=" , number * i)