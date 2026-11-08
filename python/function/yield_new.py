# write a generater function that yield even number up to a specified limit
# 1.
# def even_generator(limit):
#     for i in range(2,limit+1 , 2):
#         return li

# print(even_generator(10))



# 2.
# def even_generator(limit):
#     li = []

#     for i in range(2,limit+1,2):
#         li.append(i)

#     return li

# print(even_generator(10))

def even_generator(limit):
    for i in range(2,limit + 1,2):
        return i

for num in even_generator(10):
    print(num )