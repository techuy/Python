x = 0
while x<5:
    print(f"the current x is {x}")
    x+=1
else:
    print(f"x is less than 5")
print("---break, continue, pass---")
# Pass keyword , pass doesn't add all
x = [1,2,3]
for item in x:
    pass
print("after the loop")

print("-Continue-")
#continue
name = "TechUy"
for letter in name:
    if letter=='U': continue
    print (letter)

print("-break-")
x = 0
while x < 5:
    if x==3: break;
    print(x)
    x+=1