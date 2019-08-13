from random import randint

pc = randint(1,100)
guesses = [0]
while True:
    
    try:
        usr = int(input("Enter a number: "))
    except Exception:
        print("Invalid input..!!!")
        break;
    #check input if it is in the condition
    if usr<0 or usr>100: 
            print("OUT OF BOUNDS, Try Again")
            continue
    
    if usr == pc:
        print(f"CONGRATS you guess it in {len(guesses)} guesses!!")

    guesses.append(usr)
    print(guesses)

    if guesses[-2]:
        if abs(pc-usr) < abs(pc-guesses[-2]):
            print("WARMER")
        else:
            print("COLDER")
    else:
        if pc-usr<=10:
            print("WARM")
        else:
            print("COLD")
    pass
    
    