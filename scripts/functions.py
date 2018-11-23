import numpy as np
import shutil
import sys
import csv
def parsing(name,row1,row2):
	x=np.array([])
	y=np.array([])
	with open(name) as tsv:
	    reader = csv.reader(tsv, delimiter="\t")
	    headers=next(reader)
	    for i in reader:
	        x=np.append(x,i[row1])
	        y=np.append(y,i[row2])
	x=np.asfarray(x,float)
	y=np.asfarray(y,float)
	return x,y

def copy_pattern(name):
	path='D:\\Labs\\'
	shutil.copytree('D:\\Labs\\pattern',path+name)

if __name__ == "__main__": 
	copy_pattern(sys.argv[1])
    