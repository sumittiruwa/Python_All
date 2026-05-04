str1 = "this is a string"

# \ this is a tab for space
# \n for next line
str2 = 'hello.\n world'
print(str1)
print(str2)


# concANTATION

str3 = 'hello'
str4 = "world"
print(str3 + " " + str4)



# lenght
# -- len also count the space 

print(len(str1))


# Indexing and slicing
str5 = "python programming"
print(str5[5])
ch = str5[6]
print(ch)


# Slicing
# -- it is used to get a part of the string
# -- it is done by using the index of the string

str6 = "hello world"
print(str6[0:4]) # it will print hell
print(str6[6:11]) # it will print world


#backward slicing
print(str6[-1]) # it will print d       
print(str6[-5:-1]) # it will print worl



#string function

str9 = "i am `learning python"
print(str9.endswith("hon"))

#capatilize
str10 = "hello world"
print(str10.capitalize()) # it will print Hello world

#replace
str11 = "hello world"
print(str11.replace("world", "python")) # it will print hello python
#find
str12 = "hello world"               
print(str12.find("world")) # it will print 6

#count
str13 = "hello world"
print(str13.count("o")) # it will print 2