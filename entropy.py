from Set import *
from math import log2
def entropy(S):
  L=np.unique(S.clas)
  print(L)
  E=0 #contains entropy
  a=0 #a is index of count
  count=np.zeros(L.size,dtype=int) #number of elements of each class
  for x in S.clas:
    for clas in L:
      #count[a]=len(S.clas==clas)
      if x == clas:
        count[a]+=1
      a+=1
    a=0
  cc=S.clas.size
  for x in count:
    E=E+log2(int(x)/cc)*x/cc
  E=-E
  return E
  