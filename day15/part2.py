import networkx as nx
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra #https://stackoverflow.com/a/56313003/3667133

# Read data

lines = [list(v.strip("\n")) for v in open("input.txt", "r").readlines() if v !="\n"] #get all edges as a list of tuples

# Helpful functions

def increment_risk(num,inc): #given a point this function will increment it by a given number accounting for wrapping at 9
    if int(num)+int(inc) <=9:
        return(int(num)+int(inc))
    else:
        return(int(num)+int(inc)-9)

def createrow(mydict,startrow): #function to create each row of the large map
    finallist=mydict[startrow] #starting with a given dictionary number
    for outercol in range(startrow+1,startrow+5): #add the next 4 dictionaries to the right of it
        for rownum in range(len(mydict[outercol])):
            finallist[rownum]+=mydict[outercol][rownum] #by doing row by row concatenation
    return(finallist)

# Build the big map - general approach is create a dictionary of all grids incremented from 0 to 8 (thats whats needed for a 5x5 grid)
# Then use this dictionary to create each of the 5 rows needed.  Then stack them.

mydict=dict() #create a dictionary of incremented grids
for i in range(9): #iterate over the number of times you want to increment (need 0 to 8 for 5x5)
    print(i)
    outlines=[] #empty list of list
    for rownum,row in enumerate(lines): #iterate over each row
        newrow=[] #empty list for creating a transformed row
        for colnum,col in enumerate(row): #iterate over each col
            newrow.append(str(increment_risk(num=int(row[colnum]),inc=i))) #create a new row by iteratively incrementing and appending each point
        outlines.append(newrow) #append new row to list of lists
    mydict[int(i)]=outlines #add final list of lists to dictionary

print(mydict.keys())

lines=[] #now create the big map as a large list
for rownum in range(5):
    lines += createrow(mydict=mydict,startrow=rownum) #createrow builds a 1 x 5 map starting from a given starting point where the input map is the unit

for line in lines: #look at the final big map (doesn't look pretty for the non-test input)
    print("".join(line))

### Now just apply solution from part 1

G = nx.DiGraph() #Make a weighted graph and make it directional in case backtracking is needed

for i,row in enumerate(lines): #Add edges to the directional graph by iterating over each point.  Each node is row,column id
    for j,col in enumerate(row):
        if j <len(row)-1: #right
            G.add_edge(str(i)+","+str(j),str(i)+","+str(j+1), weight=int(lines[i][j+1]))
        if i < len(lines)-1: #down
            G.add_edge(str(i)+","+str(j),str(i+1)+","+str(j), weight=int(lines[i+1][j]))
        if j >0: #left
            G.add_edge(str(i)+","+str(j),str(i)+","+str(j-1), weight=int(lines[i][j-1]))
        if i > 0: #up
            G.add_edge(str(i)+","+str(j),str(i-1)+","+str(j), weight=int(lines[i-1][j]))

res=single_source_dijkstra(G,"0,0",str(len(lines)-1)+","+str(len(lines[0])-1)) #go from 0,0 to the bottom right corner
print(res)