from collections import deque 
from itertools import repeat
import sys

#Read data 
text_file = open("input1.txt", "r")
lines = deque(list(map(int,[v.split(",") for v in text_file.readlines()][0])))

print(lines)

acc=0
olddeque=lines
while acc<256:
    newdeque=deque()
    acc+=1
    newfish=0
    while olddeque:
        if olddeque[0]==0:
            #set to 6
            newdeque.append(6)
            newfish+=1 #bump up count for to add at the end
            olddeque.popleft()
        else:
            #set to item-1
            newdeque.append(olddeque[0]-1)
            olddeque.popleft()
    if newfish>0:
        #add a bunch of 8s
        newdeque.extend(deque(repeat(8, newfish)))
    olddeque=newdeque
    print("iteration:",acc,newfish)
    # print("After",acc,"day:",olddeque)

print("Number of fish:",len(newdeque))