from VectorFinder import *
import glob
import os

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
	file_vec = open(os.path.splitext(file_name)[0]+"_vectors.txt","w") 
	file_vec.write(str(returnList))
	del returnList[:]  
	file_vec.close()
	ins.close()
	
  

