import sys
text_file = open("input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()] #get all edges as a list of tuples

folds=[x[11:].split("=") for x in lines[lines.index("")+1:]]#separate coords and folds
lines=[list(map(int,x.split(","))) for x in lines[0:lines.index("")]]#also convert coords to int

for fold in folds[0:2]:##Get the max number of rows and columns
    if fold[0]=="x": #Ahh this frustrated me very badly because originally I just founf row and col max by getting the maxes directly from the values
        colmax=2*int(fold[1]) #this worked for the sample input but not the actual input
    elif fold[0]=='y': #That doesn't work because the last row(s) doesn't necessarily need to contain a '#'
        rowmax=2*int(fold[1]) #So you need to set the max rows/cols based on the folds happening (will always be in half)

thelist=[[" "]*(colmax+1) for _ in range(rowmax+1)] #use those to create an empty list of lists

for line in lines: #now populate it with #s
    thelist[line[1]][line[0]]="#"

def makecut(outlist,cutdir,cutloc):
    if cutdir=="y":#horizontal cut
        topleft=outlist[:cutloc]
        foldme=outlist[cutloc+1:]
    elif cutdir=="x":
        topleft=[]
        foldme=[]
        for thisline in outlist:
            topleft.append(thisline[:cutloc])
            foldme.append(thisline[cutloc+1:])
    return((topleft,foldme))

def flipit(lines,cutdir):
    if cutdir=="y":#horizontal
        outlist=[]
        for line in lines:
            outlist.insert(0,line)
    elif cutdir=="x":
        outlist=[[] for _ in range(len(lines))]
        for row in range(len(lines)):
            colnum=len(lines[0])
            for col in range(len(lines[0])):
                colnum-=1
                outlist[row].append(lines[row][colnum])
    return(outlist)

def reconcile(topleft,foldme):
    outlist=[[] for _ in range(len(topleft))]
    for row in range(len(topleft)):
        for col in range(len(topleft[0])):
            if topleft[row][col]=="#" or foldme[row][col]=="#":
                outlist[row].append("#")
            else:
                outlist[row].append(" ")
    return(outlist)

iteration=0
for fold in folds:
    iteration+=1
    print('Iteration:',iteration,"Fold:",fold)
    print("Thelist:","r:",len(thelist),"c:",len(thelist[0]))
    topleft,foldme=makecut(outlist=thelist,cutdir=fold[0],cutloc=int(fold[1])) #cut into 2 pieces

    print("Top Left:",len(topleft),len(topleft[0]))
    print("Fold Me:",len(foldme),len(foldme[0]))
    foldme=flipit(lines=foldme,cutdir=fold[0]) #rotate the piece you are folding
    thelist=reconcile(topleft=topleft,foldme=foldme)
    
    acc=0 #now count
    for line in thelist:
        acc+=line.count("#")
    print('Iteration:',iteration,"Fold:",fold,"Number of hashes:",acc)

for line in thelist:
    print("".join(line))