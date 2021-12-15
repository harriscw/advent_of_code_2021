text_file = open("input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()] #get all edges as a list of tuples

folds=[x[11:].split("=") for x in lines[lines.index("")+1:]]#separate coords and folds
lines=[list(map(int,x.split(","))) for x in lines[0:lines.index("")]]#also convert coords to int

acc=0
for fold in folds:
    newpoints=[]
    lines_to_keep=[]
    if fold[0]=="y": #a fold at y = 7 means anything < 7 is untouched, anything>7 has x coord the same but new y = totaly-y
        for line in lines:
            if line[1]<int(fold[1]): #if row is < row being folded on
                lines_to_keep.append(line) #dont change
            elif line[1] != int(fold[1]): #else if its greater than the fold row 
                lines_to_keep.append([line[0],2*int(fold[1])-line[1]]) #the new row is total rows-current row. Total rows is estimated as 2*fold row.

    elif fold[0]=="x":#Similar to above
        for line in lines:
            if line[0]<int(fold[1]): #if col is < col being folded on
                lines_to_keep.append(line) #dont change
            elif line[0] != int(fold[1]): #else if its greater than the fold col
                lines_to_keep.append([2*int(fold[1])-line[0],line[1]]) #the new col is total col-current col. Total cols is estimated as 2*fold col.

    acc+=1
    unique_data = [list(x) for x in set(tuple(x) for x in lines_to_keep)] #only keep unique points
    print("iteration:",acc,"fold:",fold,"points:",len(unique_data))
    lines=unique_data

rowmax=0 #get max rows and cols
colmax=0 #this was my original approach in my other solution that didn't work.  Fine here as we don't care about extra rows/cols with no #
for line in lines:
    rowmax=max(rowmax,line[1])
    colmax=max(colmax,line[0])

outlist=[[" "]*(colmax+1) for _ in range(rowmax+1)] #use those to create an empty list of lists

for line in lines: #now populate it with #s
    outlist[line[1]][line[0]]="#"

for line in outlist: #print the result to console
    print("".join(line))