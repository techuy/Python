# declare turple
t = (1,2,3)
# list
mydic = [1,2,3]
print(type(t),type(mydic))

#we can call each element 
t1 = ("one",2,3.00)
print(t1[0])
print(t1[-1])

#turple can know how many of same element has in the turple using count
t2 = ('a','a','b','a')
print(t2.count('a'))
# the index of the first time that appear in the turple
print(t2.index('b'))

#what make turple is that it is immubility
mydic[0]= 10 # turple cannot do that 


