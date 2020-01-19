import nltk
nltk.download('wordnet')

word = 'cardboard.n.01'
word2=''


def wordSplit(word):
	word2=''
	for i in range(len(word)):

		if word[i] != '.':
			word2+=word[i]
		if word[i]=='.':
			
			return word2
print(wordSplit(word))
#print(nltk.similar(word2))