import networkx as nx
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra #https://stackoverflow.com/a/56313003/3667133

lines = [list(v.strip("\n")) for v in open("input.txt", "r").readlines() if v !="\n"] #get all edges as a list of tuples

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