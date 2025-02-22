# Learning String concatination module
str1 = "HELLO,"
str2 = "welcome to python programming"
result = str1 + " " + str2
print(result)

# Learning length module
length = len(str2) 
print(" length of string 2 is: ", length)

# Learning Uppercase, Lowercase module
lowercase = str1.lower()
uppercase = str2.upper()
print(lowercase)
print(uppercase)

# Learning Replace module
new_text = str2.replace("welcome","Learn")
print(new_text)

# Learning Split module
word = str2.split()
print(word)

# Leraning substring module
substring = "welcome"
if substring in str2:
    print ("substring is present in str2", substring) 

