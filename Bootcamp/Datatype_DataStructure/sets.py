# how to declear set, and sets can only have on representive value , unordered element of the unique element
myset = set()
myset.add(1)
print(myset)
# in this case the another 1 doesnt add into the set
myset.add(1)
print(myset)

# we can change list to set 
mylist = [1,1,2,2,2,1,2,3,2,1,2,2,3,3,1,3,1,3]
print(set(mylist))
# in only appears 1 2 3
