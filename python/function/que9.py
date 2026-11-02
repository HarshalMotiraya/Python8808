# yield
# prob-write a generator function that yields even number up to a specified limit

# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         return i

# print(even_generator(10))


# def even_generator(limit):
#     li = []
#     for  i in range (2,limit + 1,2):
#         li.append(i)
#     return li

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i


for num in even_generator(10):
    print(num)



# yield is stored not only value but it's memory state