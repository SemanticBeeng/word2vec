from VectorFinder import *
import glob
import os
import cPickle

list_of_files = glob.glob('../data/*.vec')          
for file_name in list_of_files:
	print file_name
	ins = open(file_name, "r")
    	array = []
    	for line in ins:
        	array.append(line.rstrip())
  	del array[0]
	returnList = VectorFinder(array)
	del array[:] 
	cPickle.dump(returnList, open(os.path.splitext(file_name)[0]+"_vectors.p", 'wb')) 
	del returnList[:]  
	ins.close()
