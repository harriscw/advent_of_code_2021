#Read data 
text_file = open("input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

def find_param(lines,spot,gamma=True):
    acc1=0
    acc0=0
    for line in lines:
        # print(line,line[spot])
        if line[spot]=="1":
            acc1+=1
        else:
            acc0+=1
    if gamma==True:
        if acc0>acc1:
            outval='0'
        else:
            outval='1'
    else:
        if acc1>=acc0: #Note the change to >= here relative to part 1
            outval='0'
        else:
            outval='1'
    # print("outval:",outval)

    newlist=[] #Now that you have the most common value, return a filtered list
    for line in lines:
        if line[spot]==outval:
            newlist.append(line)
            
    return(newlist)

def runit(lines,gamma): #Now iterate position by position, filtering the list each time
    outlist=lines
    for i in range(len(lines[0])): #iterate over the length of the string
        # print(i+1,len(outlist))
        # print(outlist)
        outlist=find_param(outlist,spot=i,gamma=gamma) #find the most common value and filter the list
        if(len(outlist)==1): #if the list is down to one string, return it
            return(outlist[0])

o2=runit(lines,True)
co2=runit(lines,False)
print("o2:",o2,"\nco2:",co2,"\nFinal Answer:",int(o2,2)*int(co2,2))