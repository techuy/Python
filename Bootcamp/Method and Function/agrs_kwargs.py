
def myfunc(a,b):
    return sum((a,b))
print(myfunc(1,2))

# *args for multiple  arguments
def myfunc1(*args):
    print(args)
    return sum(args)

print(myfunc1(2,4,1,2,3,4,5,6,7,5,1,2,4,5,6))


#kwargs = keyword arguments
def myfuncKwargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("my fruit of choice is {}".format(kwargs['fruit']))
    else:
        print('i didnt find any fruit here')

myfuncKwargs(fruit='apple',veggie='lettuce')

def myhybrid(*args,**kwargs):
    print("i'd like {} {}".format(args[0],kwargs['food']))

myhybrid(10,20,30,fruit='orange',food='eggs',animal='dog')
