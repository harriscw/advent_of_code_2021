#Read data 
text_file = open("input.txt", "r")
lines = [v.strip("\n").split(" -> ") for v in text_file.readlines()]

mydict=dict() #decided to store coordinates in a dictionary to avoid determining min/max for a grid.  Plus maybe quicker with sparse data.
for line in lines:
    start=list(map(int,line[0].split(","))) #convert each line to a list of start and end points
    end=list(map(int,line[1].split(",")))
    
    if start[0]==end[0]: #handle case when x1=x2, iterating by row adding to a fixed column
        thestart=min(start[1],end[1]) #iterate from low to high
        thestop=max(start[1],end[1])
        col=start[0]
        for row in range(thestart,thestop+1): #iterate over rows
            if row in mydict.keys(): #if the row exists
                if col in mydict[row].keys():# if there's already data at that column
                    mydict[row][col]+=1 # then add to the value at that row and column
                else:
                    mydict[row][col]=1 #else if that column doesn't exist set it to 1
            else:
                mydict[row]={col:1} #else if that row doesn't exist create a sub dictionary setting that column to 1

    elif start[1]==end[1]: #handle case when y1=y2, iterating by column adding to a fixed row
        thestart=min(start[0],end[0]) #iterate from low to high
        thestop=max(start[0],end[0])
        row=start[1]
        if row in mydict.keys(): #if the row exists
            for col in range(thestart,thestop+1): #then iterate over cols
                if col in mydict[row].keys():# if there's already data at that column
                    mydict[row][col]+=1 #then add to the value at that row and column
                else:
                    mydict[row][col]=1 #else if that column doesn't exist set it to 1
        else: #else if that row doesn't exist create a sub dictionary setting all specified columns to 1
            mydict[row]=dict()
            for col in range(thestart,thestop+1):
                mydict[row][col]=1

    else:# This is where part 2 starts where we want to iterate diagonally.  I really got my coordinates confused and thus named variable poorly
        if start[0]<end[0] and start[1]<end[1]:
            thedir="down right"
            rowmod=1
            colmod=1
        elif start[0]>end[0] and start[1]<end[1]:
            thedir="down left"
            rowmod=-1
            colmod=1
        elif start[0]>end[0] and start[1]>end[1]:
            thedir="up left"
            rowmod=-1
            colmod=-1
        elif start[0]<end[0] and start[1]>end[1]:
            thedir="up right"
            rowmod=1
            colmod=-1

        newrow=start[0]
        newcol=start[1]
        for row in range(start[0],end[0]+rowmod,rowmod): #iterate over x coordinates
            if newcol in mydict.keys(): #if the dictionary entry exists
                if newrow in mydict[newcol].keys():
                    mydict[newcol][newrow]+=1
                else:
                    mydict[newcol][newrow]=1
            else:
                mydict[newcol]={newrow:1}
            newrow=newrow+rowmod
            newcol=newcol+colmod

acc=0  #now find all points where at least two lines overlap
outlist=[]
for key in sorted(mydict):
    for subkey in sorted(mydict[key]):
        outlist.append(str(subkey)+","+str(key)+"/num:"+str(mydict[key][subkey]))
        if mydict[key][subkey]>1:
            acc+=1

outlist.sort()
# for coord in outlist:
#     print(coord)    
print(acc)