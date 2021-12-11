#Read data 
text_file = open("input.txt", "r")
lines = [list(map(int,list(v.strip("\n")))) for v in text_file.readlines()]

lowpoints=[] #iterate over each point, if its lower than all neighbors (non-diagonal) write it out
for row in range(len(lines)):
    for col in range(len(lines[row])):
        acc=0 #number of neighbors the given point is less than
        total=0 #total number of neighbors that exist (e.g. first row doesn't have a neighbor above)
        if (row-1>=0): #check up
            total+=1
            if lines[row-1][col]>lines[row][col]:
                acc+=1
        if (col-1>=0): #check left
            total+=1
            if lines[row][col-1]>lines[row][col]:
                acc+=1
        if (row+1<len(lines)): #check down
            total+=1
            if lines[row+1][col]>lines[row][col]:
                acc+=1
        if (col+1<len(lines[row])): #check right
            total+=1
            if lines[row][col+1]>lines[row][col]:
                acc+=1

        if acc==total: #if the point is lower than all its neighbors then append
            lowpoints.append(lines[row][col])

print("Final Answer:",sum(lowpoints)+len(lowpoints)) #sum the list, and since we're adding 1 to each point we can just add the list length