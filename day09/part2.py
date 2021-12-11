import csv

#Read data 
text_file = open("input.txt", "r")
lines = [list(map(int,list(v.strip("\n")))) for v in text_file.readlines()]

for line in lines:
    print(line)

#lets surround it with 9s
for line in lines:
    line.insert(0,9)
    line.append(9)

ninelist=[9 for x in range(len(lines[0]))]
lines.append(ninelist)
lines.insert(0,ninelist)

print("")
for line in lines:
    print(line)

# Write out to csv to visualize
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(lines)

###
# Get low points applying part 1 solution
###

lowpoints=[] #iterate over each point, if its lower than all neighbors (non-diagonal) write it out
for row in range(len(lines)):
    for col in range(len(lines[row])):
        acc=0 #number of neighbors the given point is less than
        total=0 #total number of neighbors that exist (e.g. first row doesn't have a neighbor above)
        if lines[row][col] !=9:
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
                lowpoints.append((row,col))

print("\n",lowpoints)

###
# Create a function to find all valid neighbors of a given point
# i.e. the neighbor is in the same basin, i.e. the neighbor is in the same area bounded by 9s
###

def get_newpoints(row,col,lines):
    newpoints=[]
    if lines[row-1][col] !=9:#fill up
        newpoints.append((row-1,col))
    if lines[row+1][col] !=9:#fill down
        newpoints.append((row+1,col))
    if lines[row][col+1] !=9:#fill right
        newpoints.append((row,col+1))
    if lines[row][col-1] !=9:#fill right
        newpoints.append((row,col-1))
    
    if lines[row+1][col+1] !=9 and not (lines[row+1][col] == 9 and lines[row][col+1] == 9):#fill DR
        newpoints.append((row+1,col+1))
    if lines[row-1][col+1] !=9 and not (lines[row-1][col] == 9 and lines[row][col+1] == 9):#fill UR
        newpoints.append((row-1,col+1))
    if lines[row+1][col-1] !=9 and not (lines[row+1][col] == 9 and lines[row][col-1] == 9):#fill DL
        newpoints.append((row+1,col-1))
    if lines[row-1][col-1] !=9 and not (lines[row-1][col] == 9 and lines[row][col-1] == 9):#fill UL
        newpoints.append((row-1,col-1))

    return(newpoints)

###
# Now iterate over all low points.
# For that low point apply the function above to find all neighbors that are in the basin and add them to a list
# Keep doing this for newly found points until no new points are found
###


basin_list=[]
for point in lowpoints: #iterate over all low points previously found
    basin=[point] #we know the low point is in the basin
    newpoints=[point] #initialize a starting place
    while True:
        points_this_iteration=[]
        for newpoint in newpoints: #iterate over all previously unchecked points
            points_this_iteration += get_newpoints(row=newpoint[0],col=newpoint[1],lines=lines) #add all points found this iteration to list
        
        newpoints = list(set(points_this_iteration) - set(basin)) #Get unique new points found this iteration.  Potentially used for next iteration

        if len(newpoints)>0: #If new points were added this iteration
            basin=list(set(basin+newpoints)) #then add them to the basin list and do another iteration
        else: #otherwise we got all the points in the basin, break the loop
            print("Final basin size",len(basin),"\nFinal basin",basin,"\n")
            basin_list.append(len(basin))
            break

basin_list.sort() #ascending sort
largest3=basin_list[-3:] #get biggest 3
acc=1
for num in largest3: #find the product
    acc *= num
print("Largest 3 basin sizes",largest3,"\nFinal Answer",acc)
