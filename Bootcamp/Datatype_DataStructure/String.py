# declare string
a = 'hello'
b="world"
c='hello world'
print(a,b)
print(c)

d="i'm going to run by TechUy"
print("Hello \nWorld")
print("Hello \n World")

#check length of the string
lenH = len("hello")
print(lenH)

myString = "Hello World"
print(myString)
print(myString[-2])

# slice
myString1 = "abcdefghijklmnopqrstuvwxyz"
print(myString1[3:])
print(myString1[:3])
print(myString1[3:6])
print(myString1[3:9])
#slice step
print(myString1[::3]) # jump from a To d (means that it will skip 3 index )
print("---------------")
# to change the string is to creating new string 
strrr = "he is iron man"
change = strrr[2:]
print(change)
change = 'Uy ' + change
print(change)
# using * to repeat the string 
print('b'*20)

print("--------------------")
x = "Hello World"
#upper
print(x.upper()) 
print(x.split())