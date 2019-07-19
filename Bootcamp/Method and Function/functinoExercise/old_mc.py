string = "abcdefg"
def old_macdonald(name='abcdefg'):
    newName = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return newName

print(old_macdonald('macdonald'))
    