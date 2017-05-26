from VectorFinder import *

file = open("../data/vectors.txt","w") 
with open("../data/word.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.rstrip())
del array[0]

returnList = VectorFinder(array)
file.write(str(returnList))  
file.close() 
