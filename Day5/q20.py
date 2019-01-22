# Ask the user for a string and print out whether this string is 
# a palindrome or not. (A palindrome is a string that reads the 
# same forwards and backwards.)
mystring = input()
for i in range(len(mystring) // 2):
    if mystring[i] != mystring[- 1 - i]:
        print('Not Palindrome')
        break
else:
    print('Palindrome')


string = "Hello"
i = 0
for ch in range(len(string)):
    if (string[i] != string[-1-i]):
        print('Not Palindrome')
        break    
    else:
        print("Pelindrom")   
        break


def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
		return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')