from random import randint
try:
    UserIn = int(input("Enter a number:"))
except Exception:
    print("Invalid input")
for _ in range (0,UserIn):
    print(randint(1,100))