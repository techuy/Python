
def paper_doll(text):
    newString = ''
    for i in text:
        newString= newString + i + i +i
    return newString

print(paper_doll("Hello"))