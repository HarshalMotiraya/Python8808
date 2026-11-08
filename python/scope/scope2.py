
# y = 12
# def f1():
#     x = 88
#     # return
#     def f2():
#         print(x)
#     return f2
# myResult = f1()
# myResult()

# closer / factory function
def chaiCoder(num):
    def actual(x):
        return x ** num 
    return actual

def chaiCoder(num):
    def actual(x):
        return x ** num 
    return actual

f = chaiCoder(2)
g = chaiCoder(3)

print(f(3))
print(g(3))