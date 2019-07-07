# retriving data by calling the key value name
my_dict = {'key':'value1','key1':'value1'}
print(my_dict['key'])

my_dicNum = {'apple':2.99,'orange':3.00}
print(my_dicNum['apple'])

# we can store array and dictionaries in a dictionaries
my_hybridDic = {'k1':'hello','k2':[2,3,4,5],'k3':{'uy':'lav'}}
print(my_hybridDic['k2'][2])
print(my_hybridDic['k3']['uy'])

# step by step assignment
d = {'k1':['a','b','c', 'd']}
d1 = d['k1']
print(d1)
letter = d1[2]
print(letter.upper())
print(d['k1'][1].upper())

# we can also add the element to the key value
d2 = {'k1':'ello'}
d2['k2'] = 200
print(d2)
d2['k1'] = 'hello'
print(d2)

# to knwo the key and value we use and list all the item
print(d2.keys())
print(d2.values())
print(d2.items())