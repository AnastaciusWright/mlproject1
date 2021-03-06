from entropy import *
import numpy as np
from Set import *

def listToSet(List):
	temp=Sets()
	for elem in List:
		temp.addElement(elem)
	return temp

def gain(dataSet, Attr):
	ent=entropy(dataSet)
	i=0
	j=0
	#First, we need to obtain the number of unique values for the attribute. The attribute must be given as a number
	attColumn=dataSet.getAttColumn(Attr)
	print("attcolumn")
	print(attColumn)
	print("--")
	lonelyValues=np.unique(attColumn) #get the unique values for the attribute
	print("Lonely values")
	print(lonelyValues)
	print("----")
	sums=np.zeros(len(lonelyValues), dtype=int) #get the count of how many times each attribute repeats in the column
	print("Sums")
	print(sums)
	print("---")
	subsets_list=[]# list of lists of elements
	subsets=[]
	for j in range(0,len(sums)): #check every possible value
		print("printing elements")
		temp_list=[]
		for i in range(0,attColumn.size): #check the entire column
			if attColumn[i] == lonelyValues[j]:
				sums[j]=sums[j]+1
				temp_list.append(dataSet.elements[i])
				#temp_Set.addElement(dataSet.elements[i])
		subsets_list.append(temp_list)
	for x in subsets_list:
		#temp_set=Sets()
		for y in x:
			y.printElement()
	##Hasta aca, tenemos las listas andando

	right_term=0
	for j in range(0,len(sums)):
		print("sums j/len(attColumn")
		print(sums[j]/len(attColumn))
		print("---")
		print("entropy of subset")
		print(entropy_list(subsets_list[j]))
		print("---")
		right_term=right_term-(sums[j]/len(attColumn))*entropy_list(subsets_list[j])
	
	return ent+right_term
