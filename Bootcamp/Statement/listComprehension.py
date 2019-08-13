myString = "Hello"

mylist = [x for x in myString]
print(mylist)

EvenNumber = [x for x in range(0,11) if x%2==0]
print(EvenNumber)

SquareNumber = [x**2 for x in range(0,11)]
print(SquareNumber)

#nested loop in list comprehension
nestedNum = [x*y for x in [1,2,3] for y in [10,11,12]]
print(nestedNum)

nestedNum1 = [x+y for x in [1,2,3] for y in [10,11,12]]
print(nestedNum1)