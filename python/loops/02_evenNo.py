# sum of even number 
# problem : Calculate the sum of even number up  to given number n.

n = 10 

sum_even = 0 

for i in range(1, n+1 ):
    if i % 2 == 0 :
        sum_even += 1

print("sum of even number is :",sum_even)