import numpy as np
import csv
def parsing(name,row1,*args):
	x=np.array([])
	y=np.array([])
	row2=args[0]
	with open(name) as tsv:
	    reader = csv.reader(tsv, delimiter="\t")
	    headers=next(reader)
	    # print(headers)
	    for i in reader:
	        x=np.append(x,i[row1])
	        y=np.append(y,i[row2])
	x=np.asfarray(x,float)
	y=np.asfarray(y,float)
	return x,y

