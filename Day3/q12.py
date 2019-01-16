# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
s = input()
dl = {'digits':0,'letters':0}
for c in s:
    if c.isdigit():
        dl["digits"]+=1
    elif c.isalpha():
        dl["letters"]+=1
    else:
        pass

print("Letters: ",dl['letters'])
print("Digits: ",dl['digits'])