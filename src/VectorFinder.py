from gensim.models.keyedvectors import KeyedVectors

file_log = open("../data/log.txt","a") 

model = KeyedVectors.load_word2vec_format('../data/text8-vector.bin', binary=True)

def VectorFinder(word_list):
	listoflists = []
	listofwords = []
	wordList = word_list
	for word in wordList:
		word = word.lower()
		try:
			v =  model[word]  # raw numpy vector of a word
			listofwords.append(word)
			listoflists.append(v)
			file_log.write("Word "+ word + " is sucessfully found in the model.\n")  
		except:
			print "Word " + word + " is not in the trained model."
			file_log.write("Word " + word + " is not in the trained model\n")  
	listoflists.append(listofwords)
	return listoflists;

 








