con = True
while (con):
    userIn = input("Enter a Number:")
    if(userIn != 'EXIT'):
        try:
            userIn = int(userIn)
            if(userIn%2==0): print(f"{userIn} is EVEN")
            else: print(f"{userIn} is ODD")
        except Exception:
            if userIn != '':
                print(f"{userIn} is not a valid number")
    elif userIn=='EXIT': break 
