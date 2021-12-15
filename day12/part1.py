#Read data 
text_file = open("input.txt", "r")
lines = [list(v.strip("\n").split("-")) for v in text_file.readlines()] #get all edges as a list of tuples

nodes=[] #get unique nodes as a single list
for line in lines:
    nodes=list(set(nodes+list(line)))

mydict=dict() #populate a dictionary with key as each node and value as a list of all connections to that node
for node in nodes:
    mydict[node]=[] #add the node to the dictionary
    for line in lines: #iterate over all lists of connections
        if node in line: #if the node is in that connection
            mydict[node]+=list(set([node]) ^ set(line)) #add the other node to the value list

def is_a_small_cave(string): #function to check if a node is a small cave
    return(all(c.islower() for c in string.strip())) #it looks to see if all characters are lowercase in the node string

pathlist=[["start"]] # initialize a path list
finalpaths=[] #initialize list for final paths
i=0
while True: #continually grow all valid paths until there's no growing paths
    i+=1
    print(i)
    newpathlist=[]
    for path in pathlist: #iterate over each path
        for nextstep in mydict[path[-1]]: #iterate over each potential next step for the last node added to the path
            ## Rules: Can't go back to "start", the prior step isn't "end", not a small cave thats already been visited
            if nextstep != "start" and path[-1] != "end" and not (is_a_small_cave(nextstep) and nextstep in path):
                newpath=path+[nextstep] #add the next node if it meets the criteria
                newpathlist.append(newpath) #and append it to the list of growing paths this iteration
                if newpath[-1]=="end": #if we got to the end then write it out to the final list
                    finalpaths.append(newpath)
    if len(newpathlist)==0: #stop if no paths are still growing
        break
    else:
        pathlist=newpathlist #reset pathlist for next iteration

print("Final Answer",len(finalpaths))