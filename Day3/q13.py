# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

w = input()
case = {"UPPERCASE":0,"LOWERCASE":0}
for word in w:
    if word.isupper():
        case["UPPERCASE"]+=1
    elif word.islower():
        case["LOWERCASE"]+=1
    else:
        pass
    

print("Upper Case: ",case["UPPERCASE"])
print("Lower Case: ",case["LOWERCASE"])
    