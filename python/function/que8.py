# function woth **kwargs
# problem:create a function that accepts any  number of keyword arguments and print  them in the formate key:value.

def print_kwargs(**kargs):
    for key, value in kargs.items():
        print(f"{key}: {value}")

print_kwargs(name="shaktiman", power="lazer")
print()
print_kwargs(name="shaktiman")
print()
print_kwargs(name="shaktiman", power="lazer", enemy="Dr.Jackaal")