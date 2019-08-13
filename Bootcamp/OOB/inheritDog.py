class Dog:
    #Class artribute
    species = "mammal"

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def description(self):
        print("{} is {} years old".format(self.name,self.age))

    def speak(self, sound):
        print("it barks {}".format(sound))

class BullDog(Dog):
    def run(self,speed):
        print("{} runs {}".format(self.name,speed))

jonh = BullDog("jonh",10)
jonh.description()
jonh.run("fast")