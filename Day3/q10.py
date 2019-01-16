# Question:

# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again

# Then, the output should be:

# again and hello makes perfect practice world

word = sorted(list(set(input().split())))              #  input string splits -> converting into set() to store unique
                                                       #  element -> converting into list to be able to apply sort 
print(" ".join(word))
