from collections import deque 

#Read data 
text_file = open("input.txt", "r")
lines = deque(list(map(int,[v.split(",") for v in text_file.readlines()][0])))

print(lines)

acc=0
olddeque=lines
while acc<80:
    # print("After",acc,"day:",olddeque)
    newdeque=deque()
    acc+=1
    newfish=0
    for item in olddeque:
        if item-1<0:
            #set to 6
            newdeque.append(6)
            newfish+=1#bump up count for to add at the end
        else:
            #set to item-1
            newdeque.append(item-1)
    if newfish>0:
        #add a bunch of 8s
        for eight in range(newfish):
            newdeque.append(8)
    olddeque=newdeque

print("Number of fish:",len(newdeque))