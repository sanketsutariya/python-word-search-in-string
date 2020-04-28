import re

string = input('Enter string: ')
word = input('Enter search word: ')

string = re.sub('a-zA-Z0-9 \n\.]','',string)

string = ''.join(i for i in string if not i.isdigit())

def search_word(string,word):
	i = 0
	z = len(word)
	max_i = len(string)-z
	
	while i<=max_i :
		if string[i:z].lower() == word.lower():
			return True
		i = i+1
		z = z+1
	return False

if search_word(string,word)==True:
	print(word + ' is found in ' + string)
else:
	print(word + ' is not found in ' + string)