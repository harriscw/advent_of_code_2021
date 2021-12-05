#Read data 
text_file = open("input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

# Parse instructions
instrux=list(map(int,lines[0].split(",")))
del lines[0]

# Parse each bingo card
mydict = {}
acc=0
thislist=[]
for i,line in enumerate(lines):
    if line=="":
        continue
    else:
        lineedit=list(map(int,line.strip().replace("  "," ").split(" "))) #get rid of whitespace, convert to int
        thislist.append(lineedit)
        if len(thislist)==5: #add to dictionary when you have a card with 5 rows
            mydict[acc]=thislist
            acc+=1
            thislist=[] #reset

def numberchanger(numtofind,thecard): #function to iterate over the card and zero out the given number
    for row in range(len(thecard)):
        for col in range(len(thecard[row])):
            if thecard[row][col]==numtofind:
                thecard[row][col]=0
    return thecard

def colsum(thecard): #function to get column sums for the bingo card for a list of lists (probably easier to use pandas here)
    for col in range(len(thecard[0])):
        thesum=0
        for row in range(len(thecard)):
            thesum+=thecard[row][col]
        if thesum==0:
            return(col) #returns the column number if it funds a 0 sum
    return(-1) #or a negative if it doesn't

def rowsum(thecard): #function to get row sums for the bingo card for a list of lists
    for row in range(len(thecard)):
        if sum(thecard[row])==0:
            return(row) #returns the row number if it funds a 0 sum
    return(-1) #or a negative if it doesn't

def check_for_zeros(thecard): #function to check both columns and rows for zero sums
        rownum=rowsum(thecard=thecard)
        if rownum >= 0:
            return ("row",rownum)

        colnum=colsum(thecard=thecard)
        if colnum >= 0:
            return ("col",colnum)
        return ("nil",-1)

for i,thenum in enumerate(instrux): #iterate over instructions
    for j,card in enumerate(mydict): #iterate over all cards
        mydict[j]=numberchanger(numtofind=thenum,thecard=mydict[j]) #zero out the current number
        res=check_for_zeros(thecard=mydict[j]) #now check for rows/cols that are all zeros
        if res[0] != "nil":
            thesum=sum(sum(x) for x in mydict[j])
            print("Got one on card:",j,"\n",res,"\n",mydict[j],"\nCard Sum:",thesum,"\nFinal Answer:",thesum*thenum)
            break
    else:
        continue
    break