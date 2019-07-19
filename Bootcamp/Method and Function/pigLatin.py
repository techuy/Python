mystring = "word"
mystring1 = "apple"

def pigLatin(string):
    # if(string[0]=='a'or string[0]=='e'or string[0]=='o'or string[0]=='i'or string[0]=='u'):
    #     return string+"ay"
    # else:
    #     return string[1::]+string[0]+"ay"
    if string[0] in "aeiou":
        pig_word = string+"ay"
    else:
        pig_word = string[1:]+string[0]+ "ay"
    return pig_word


print(pigLatin(mystring))
print(pigLatin(mystring1))