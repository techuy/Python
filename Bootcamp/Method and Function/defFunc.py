def name_function():
    """
    This Function is to call Hello
    """
    print("Hello World")

name_function()
# help(name_function)

print("---------")
def say_hello(name="NAME"):
    print('Hello '+name)

say_hello("TechUy")

def return_lll(name):
    return "Hello "+name
print(return_lll("Uy"))

def dog_check(mystring):
    return "dog" in mystring
print(dog_check("my dog has fur"))