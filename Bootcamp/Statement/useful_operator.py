mylist = []
for num in range(10):
    mylist.append (num)
print(mylist)

# the better way to do it and the end of index isn't counting
mylist1 = list(range(0,10))
print(mylist1)

print("-------")
index_count = 1
for letter in 'abcdefghijklmnopqrstuvwxyz':
    print(f"the index of {letter} is {index_count}")
    index_count+=1
# we can use
index_count=0
word = "abcdefghijklmnopqrstuvwxyz"
for _ in word:
    print(word[index_count])
    index_count+=1

print(" -------- ")
#enumerate
for index,item in enumerate(word):
    print(item)
    print(index)
    print("\n")

        
print(" -------Zip------ ") # zip only return the list that is the shortest
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300,400,500,600]
print(zip(mylist1,mylist2))
for item in zip(mylist1,mylist2):
    print(item)
overList = list(zip(mylist1,mylist2,mylist3))
print(overList)

print(" ------ ")
# in keyword 
print('x' in [1,2,3])
print('x' in [ 'y',' y','x'])
# in can also use in dictionaries
print('key1' in {'key1':345})
print(345 in {'key1':345}.values())
print(345 in {'key1':345}.keys())

#mininum function in list
mylist5 = [100,200,300,2,0,150]
print(min(mylist5))
print(max(mylist5))
