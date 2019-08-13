
result = 0
while(True):
    UserIn = input("Enter a number:")
    if(UserIn!='exit' and UserIn!=''):
        UserIn = int(UserIn)
        result+=UserIn
        print(f"TOTAL: {result}")
        continue
    elif(UserIn==''):
        print(f"TOTAL: {result}")
        continue
    elif UserIn=='exit': break