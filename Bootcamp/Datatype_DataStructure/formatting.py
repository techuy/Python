# format is used to insert the string base on the curly brace
print("string is {} printed ".format('insert'))
print("string is  printed {}".format("insert"))

# we can insert base on the inedex
print('The {} {} {}'.format("bronw","quick","fox"))
print('The {1} {0} {2}'.format("bronw","quick","fox"))
hello = 'The {1} {0} {2}'.format("bronw","quick","fox")
print('The {q} {b} {f}'.format(b= "bronw",q="quick",f="fox"))
print('The {f} {f} {f}'.format(b= "bronw",q="quick",f="fox"))

#float formatting 
result = 100/77
print(result)
print("this result of this is {r}".format(r=result))
# follow {value:width.precision f}
# width is like the length of the string that we want it to have
# if it over , it will add space
print("this result of this is {r:0.3f}".format(r=result))

#another way to do format 
print("string is printed {0:10}".format("inserthellnoo"))



# the new way to format in python 3 is just add print(f"hell {no }") 
print("--------------------")
name = "techUy"
print(f"hello this is {name}")
