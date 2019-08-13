class Dog:
    def __init__(self,name,age):
       self.name = name
       self.age = age
    
jonhny = Dog("jonhy",10)
milky = Dog("milky",12)
doggie = Dog("doggie",15)

def get_the_biggest_number(*args):
    # answer = 0 
    # if(args[0]>args[1] and args[0]>args[2]): answer = args[0]
    # elif(args[1]>args[0] and args[1]>args[2]): answer = args[1]
    # else: answer = args[2]
    return max(args)
    

print("The oldest dog is {} years old".format())
