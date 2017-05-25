from gensim.models.keyedvectors import KeyedVectors

listoflists = []
model = KeyedVectors.load_word2vec_format('../data/text8-vector.bin', binary=True)

def VectorFinder(word_list):
	wordList = word_list
	for word in wordList:
		v =  model[word]  # raw numpy vector of a word
		listoflists.append(v)
	return listoflists;





