mylist = [1,2,3,4,5,6,7,8,9,10]
for item in mylist:
    print(item)

print("-----")

for num in mylist: 
    #check even
    if num%2==0: print(num)
    else: print(f'odd numer {num}')

print("-----")

list_sum = 0
for num in mylist:
    list_sum+=num
print(list_sum)

print("---String in forLoop---")
mystring = "hello world"
for letter in mystring:
    print(letter)

print("--tuples in for loop--")
t = (1,2,3)
for i in t:
    print(i)
print("--tuple packing--")
mylist = [(1,2),(3,4),(5,6),(7,8)]
for i in mylist:
    print(i)
print("--")
# the packing is
for (a,b) in mylist:
    print(a)
    print(b)
print("--for dictionaries--")
d = {'k1':'value1','k2':'value2','k3':'value3'}
for i in d.items():
    print(i)
print("--better usage--")
for key,value in d.items():
    print(value)
for value in d.values():
    print(value)