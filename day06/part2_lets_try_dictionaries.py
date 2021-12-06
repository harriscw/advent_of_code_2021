from collections import deque 
from itertools import repeat
import sys

#Read data 
text_file = open("input1.txt", "r")
lines = list(map(int,[v.split(",") for v in text_file.readlines()][0]))

mydict=dict()
for i,line in enumerate(lines):
    mydict[i]=line

print(mydict)
acc=0
newkeymax=len(mydict.keys())
while acc<256:
    acc+=1
    newfish=0
    keymax=0
    for i in range(newkeymax):
        keymax+=1
        # print(i)
        if mydict[i]==0:
            mydict[i]=6
            newfish+=1 #bump up count for to add at the end
        else:
            #set to item-1
            mydict[i]=mydict[i]-1
    if newfish>0:
        #add a bunch of 8s
        newkeymax=keymax+newfish
        for j in range(keymax,newkeymax):
            mydict[j]=8
    # print("iteration:",acc,mydict.values())
    print("iteration:",acc)

print("Number of fish:",len(mydict.keys()))
