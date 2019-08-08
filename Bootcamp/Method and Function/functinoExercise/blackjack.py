def blackjack(a,b,c):
    d = a+b+c
    
    if(d<=21):
        return f"{d}"
    else:
        if(a==11 or b==11 or c==11):
            d-=10
            if(d>21): return f"BUST"
            else: return f"{d}"
        else:
            return "BUST"
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
