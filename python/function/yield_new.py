# write a generater function that yield even number up to a specified limit

def even_generator(limit):
    for i in range(2,limit+1 , 2):
        print(i)
        