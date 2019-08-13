class pets:
    dogs = []
    def __init__(self, dogs):
        self.dogs = dogs



# Parent class
class Dog:

    # Class attribute
    is_Hungry = True
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_Hungry = False

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)



dogs = [
    Bulldog("Jack",10),
    Dog("Mike",1),
    RussellTerrier("Doe",5)
]

pets1 = pets(dogs)

print("I have {} dogs".format(len(pets1.dogs)))
for dog in pets1.dogs:
    dog.eat()
    print("{} is {} years old".format(dog.name,dog.age))

print("and they are all {}, of courese".format(dog.species))

are_dog_hungry = False
for dog in pets1.dogs:
    
    if dog.is_Hungry:
        are_dog_hungry = True

if are_dog_hungry:
    print("My dogs are hungry")
else:
    print("My dogs are not hungry")
