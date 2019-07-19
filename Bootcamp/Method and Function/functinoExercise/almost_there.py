def almost_there(number):
    if number<=100 and number%10 ==0:
        b = True
    elif(number>101 and number <=110) : b =  True
    elif (number>201 and number<=210):  b = True
    else: b = False
    return b 

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print(almost_there(90))