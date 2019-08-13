# list is like array but it's dynamic because we can store any datatype
my_list = ["String",1,5.0]

mylist = ["zero","one","two"]
print(mylist[0])
#concate list
print(mylist+my_list)

# change 
mylist[0]="ONEEEE"
print(mylist)

# append is like "push" add the end of the list
mylist.append("four")
print(mylist)

#remove element from the list
mylist.pop()
pop_list = mylist.pop()
print(mylist) 
print(pop_list)
# we can remove the element base on the index
mylist.pop(1)
print(mylist)

#sort and reverse
new_list = ['a','v','d','b','f']
numlist = [1,3,5,2,10,8,12]
numlist.sort()
new_list.sort()
print(numlist) 
print(new_list)
numlist.reverse()
new_list.reverse()
print(numlist) 
print(new_list)