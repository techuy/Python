 # we use file to interact with external file on our computer

# when we read the file, it show the text in the file in one line and the cursor will move to the end of the text
# to reset the cursor we used seek, file.seek(0)

# readline method is split the space into the list

file = open("D:\\KIT\\self-study\\Python\\Bootcamp\\Datatype_DataStructure\\test.txt")
print(file.read())
print(file.read())
# seek move the cursor to the beginning
file.seek(0)
print(file.read())
# if we dont use close, when you delete the file it will popup saying python still using the file
file.close()

print("---------------------------------")
# a new way to file, after as it is the variable name we want so i give it myfile
with open("D:\\KIT\\self-study\\Python\\Bootcamp\\Datatype_DataStructure\\test.txt") as myfile:
    contents = myfile.read()
print(contents)

# we can also write the file and overwrite the file, in defualt the mode is 'r'
with open ("D:\\KIT\\self-study\\Python\\Bootcamp\\Datatype_DataStructure\\newfile.txt",mode='r') as myfile:
    print(myfile.read())
print('-------------')
with open ("D:\\KIT\\self-study\\Python\\Bootcamp\\Datatype_DataStructure\\newfile.txt",mode='a') as f:
    f.write('\n4 Line')
print('-----------')
with open ("D:\\KIT\\self-study\\Python\\Bootcamp\\Datatype_DataStructure\\newfile.txt",mode='r') as myfile:
    print(myfile.read())
# write file
with open("D:\\KIT\\self-study\\Python\\Bootcamp\\Datatype_DataStructure\\newfile.txt",mode='w') as f:
    f.write('The file is created')
with open("D:\\KIT\\self-study\\Python\\Bootcamp\\Datatype_DataStructure\\newfile.txt",mode='r') as f:
    print(f.read())