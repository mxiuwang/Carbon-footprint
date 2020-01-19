import nltk
nltk.download('wordnet')

word = 'cardboard.n.01'
word2=''

for i in range(len(word)):
	while word[i] != '.':
		word2+=word[i]
		
print(word2)