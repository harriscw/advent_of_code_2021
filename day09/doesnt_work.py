#Read data 
text_file = open("input1.txt", "r")
lines = [list(map(int,list(v.strip("\n")))) for v in text_file.readlines()]

lowpoints=[] #iterate over each point, if its lower than all neighbors (non-diagonal) write it out
acc=0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] != 9:
            lines[row][col]=1
            acc+=1
        elif lines[row][col] ==9:
            lines[row][col]=0

#lets surround it with 0s
for line in lines:
    line.insert(0,0)
    line.append(0)

zerolist=[0 for x in range(len(lines[0]))]
lines.append(zerolist)
lines.insert(0,zerolist)


for line in lines:
    print(line)

#for each non 0 point, iterate in each direction until you find a 0.
#iterate up,down,left,right,ur,lr,ul,ll until you find a 0

def sum_down(line,row,col):
    acc=0
    # print("Row, Col:",(row,col),"val:",lines[row][col])
    if lines[row][col]==0:
        return(0)
    else:
        for subrow in range(row,len(lines)):
            if lines[subrow][col] !=0:
                acc+=1
            else:
                # print((subrow,col,lines[subrow][col]),acc)
                return(acc)

def sum_below(line,row,col):
    acc=0
    # print("Row, Col:",(row,col),"val:",lines[row][col])
    if lines[row][col]==0:
        return(0)
    else:
        for subrow in range(row,len(lines)):
            if lines[subrow+1][col] !=0:
                acc+=1
            else:
                # print((subrow,col,lines[subrow][col]),acc)
                return(acc)

def sum_above(line,row,col):
    acc=0
    # print("Row, Col:",(row,col),"val:",lines[row][col])
    if lines[row][col]==0:
        return(0)
    else:
        for subrow in range(row,-1,-1):
            if lines[subrow-1][col] !=0:
                acc+=1
            else:
                # print((subrow,col,lines[subrow][col]),acc)
                return(acc)

def sum_right(line,row,col):
    acc=0
    # print("Row, Col:",(row,col),"val:",lines[row][col])
    if lines[row][col]==0:
        return(0)
    else:
        for subcol in range(col,len(lines[0])):
            if lines[row][subcol+1] !=0:
                acc+=1
            else:
                # print((subrow,col,lines[subrow][col]),acc)
                return(acc)

def sum_left(line,row,col):
    acc=0
    # print("Row, Col:",(row,col),"val:",lines[row][col])
    if lines[row][col]==0:
        return(0)
    else:
        for subcol in range(col,-1,-1):
            if lines[row][subcol-1] !=0:
                acc+=1
            else:
                # print((subrow,col,lines[subrow][col]),acc)
                return(acc)

def sum_DR(line,row,col):
    acc=0 
    # print("Row, Col:",(row,col),"val:",lines[row][col])
    if lines[row][col]==0:
        return(0)
    else:
        iteration_nums=min(len(lines[0])-col,len(lines)-row)
        for i in range(iteration_nums):
            # print((subrow+1,subcol+1,lines[subrow+1][subcol+1]),acc)
            if lines[row+i+1][col+i+1]==0 or (lines[row+i+1][col]==0 and lines[row][col+i+1]==0): #modification to account for diagonal boundaries
                return(acc)
            else:
                acc+=1

def sum_UR(line,row,col):
    acc=0 
    # print("Row, Col:",(row,col),"val:",lines[row][col])
    if lines[row][col]==0:
        return(0)
    else:
        iteration_nums=min(len(lines[0])-col,row)
        for i in range(iteration_nums):
            # print((row-i-1,col+i+1))
            if lines[row-i-1][col+i+1]==0 or (lines[row-i-1][col]==0 and lines[row][col+i+1]==0): #modification to account for diagonal boundaries
                return(acc)
            else:
                acc+=1

def sum_DL(line,row,col):
    acc=0 
    # print("Row, Col:",(row,col),"val:",lines[row][col])
    if lines[row][col]==0:
        return(0)
    else:
        iteration_nums=min(col,len(lines)-row)
        for i in range(iteration_nums):
            # print((subrow+1,subcol+1,lines[subrow+1][subcol+1]),acc)
            if lines[row+i+1][col-i-1]==0 or (lines[row+i+1][col]==0 and lines[row][col-i-1]==0): #modification to account for diagonal boundaries
                return(acc)
            else:
                acc+=1

def sum_UL(line,row,col):
    acc=0 
    # print("Row, Col:",(row,col),"val:",lines[row][col])
    if lines[row][col]==0:
        return(0)
    else:
        iteration_nums=min(col,row)
        for i in range(iteration_nums):
            # print((subrow+1,subcol+1,lines[subrow+1][subcol+1]),acc)
            if lines[row-i-1][col-i-1]==0 or (lines[row-i-1][col]==0 and lines[row][col-i-1]==0): #modification to account for diagonal boundaries
                return(acc)
            else:
                acc+=1

outlist=[]
for row in range(len(lines)): #iterate over each point
    for col in range(len(lines[row])):
        downsum=sum_below(line=line,row=row,col=col)
        upsum=sum_above(line=line,row=row,col=col)
        rightsum=sum_right(line=line,row=row,col=col)
        leftsum=sum_left(line=line,row=row,col=col)
        drsum=sum_DR(line=line,row=row,col=col)
        ursum=sum_UR(line=line,row=row,col=col)
        dlsum=sum_DL(line=line,row=row,col=col)
        ulsum=sum_UL(line=line,row=row,col=col)

        total=sum([downsum,upsum,rightsum,leftsum,drsum,ursum,dlsum,ulsum]) #need to add 1 for the spot itself
        outlist.append(total) 

    #     if row==1 and col==2:
    #         break
    # else:
    #     continue
    # break

new_list = [outlist[i:i+len(lines[0])] for i in range(0, len(outlist), len(lines[0]))]
print("")
for line in new_list:
    print(line)


