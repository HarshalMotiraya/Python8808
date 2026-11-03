

def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")



print_kwargs(power =" shaktiman " , name  = "lite_lazer" ) 
print_kwargs(name = "shaktiman",power= "lazer " , enemy ="dr.jakaal")
