def has_33(numbers):
    for i in range(0,len(numbers)-1):
        if(numbers[i]==3 and numbers[i+1]==3):
            b = True
        else:
            b = False
    return b

print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))