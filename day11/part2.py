import sys
#Read data 
text_file = open("input.txt", "r")
lines = [list(map(int,list(v.strip("\n")))) for v in text_file.readlines()]

def explode(row,col,lines): #Given the point is a 9 add 1 to all surrounding points
    width=len(lines[0])
    height=len(lines)

    lines[row][col]=0 #set this point to 0
    
    if col-1 >=0 and lines[row][col-1]!=0:
        lines[row][col-1]+=1 #Left
    if col+1 < width and lines[row][col+1]!=0:
        lines[row][col+1]+=1 #right

    if row-1 >= 0: # Do row above
        if lines[row-1][col]!=0:
            lines[row-1][col]+=1 #up
        if col-1 >=0 and lines[row-1][col-1]!=0:
            lines[row-1][col-1]+=1 #UL
        if col+1 < width and lines[row-1][col+1]!=0:
            lines[row-1][col+1]+=1 #UR
        
    if row+1 < height:# Do row below
        if lines[row+1][col]!=0:
            lines[row+1][col]+=1 # down
        if col-1 >=0 and lines[row+1][col-1]!=0:
            lines[row+1][col-1]+=1 #DL
        if col+1 < width and lines[row+1][col+1]!=0:
            lines[row+1][col+1]+=1 #DR

    return(lines)

iterations=0
total_nines=[]
while True: #For part 2 dont stop at 100 iterations

    #first add 1 to every point
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            lines[row][col]+=1
    
    #Now search for 9s and explode them
    nines_this_iteration=[]
    while True: #search while number of 9s is >0 
        num9s=0  
        for row in range(len(lines)):  # go point by point looking for 9s to explode
            for col in range(len(lines[0])):
                if lines[row][col]>9: #if you find a 9
                    lines=explode(row=row,col=col,lines=lines) #explode it
                    num9s+=1 #add one to the count of points you exploded
        if num9s>0: #if you found 9s this iteration add the number to the running list and keep going
            nines_this_iteration.append(num9s)
        else: #everything has exploded this iteration, go to the next one
            total_nines.append(sum(nines_this_iteration)) 
            iterations+=1
            totalsum=0 #here's the part 2 modification: find the sum of all octos
            for row in range(len(lines)):
                totalsum+=sum(lines[row])
            if totalsum==0: #if the sum is 0 then they all flashed this turned
                print("Stopped After Step:",iterations) #return the iteration number
                sys.exit()      #and stop
            break