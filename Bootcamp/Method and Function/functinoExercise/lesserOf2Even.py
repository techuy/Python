def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a<b: c = a
        else: c =b
    else:
        if a<b: c = b
        else: c =a
    return c

lesser_of_two_evens(2,4) # -> 2
lesser_of_two_evens(2,5) #-> 5
