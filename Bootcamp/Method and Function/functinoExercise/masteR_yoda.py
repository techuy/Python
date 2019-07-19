def master_yoda(text="abc"):
     text = text.split()
     text.reverse()
     b = " ".join(text)
     return b

     
print(master_yoda("i am home"))
print(master_yoda("we are ready"))