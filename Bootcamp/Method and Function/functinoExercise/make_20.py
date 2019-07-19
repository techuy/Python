def makes_twenty(n1,n2):
    if n1+n2==20 or n1==20 or n2==20:
        b = True
    else:
        b =False
    return b

makes_twenty(20,10) #--> True
makes_twenty(12,8) #--> True
makes_twenty(2,3) #--> False