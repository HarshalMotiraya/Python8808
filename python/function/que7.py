# problem- function with *args
# write a function that takes variable number of arguments and return their sum.

def summ_all(*args):
    return sum(args)
    

print(summ_all(1,2))
print(summ_all(1,2,3,4,5))
print(summ_all(1,2,3,4,5,6,7,8))

