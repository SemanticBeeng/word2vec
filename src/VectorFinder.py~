import re

f = open('../data/text8-vector.txt', "r")
searchlines = f.readlines()
f.close()

listoflists = []

def ConvertStringToFloat(str):
   for k in range(1,len(str),1):
	str[k] = float(str[k])
   return str


def VectorFinder(word_list):
	wordList = word_list
	for word in wordList:
		for i, line in enumerate(searchlines):
    			if (re.findall('\\b'+word+'\\b', line)): 
        			for l in searchlines[i:i+1]: 
        				splitted_list =l.split()
					splitted_list = ConvertStringToFloat(splitted_list)
		listoflists.append(splitted_list)
	return listoflists;






