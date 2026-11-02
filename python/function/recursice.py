# create a recursive function to calculate the  fctorial of a number .

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    