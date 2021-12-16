from collections import Counter
text_file = open("input.txt", "r")
lines = [v.strip("\n").split(" -> ") for v in text_file.readlines() if v !="\n"] #get all edges as a list of tuples

template=lines[0][0]
mydict={item[0]:item[1] for item in lines[1:]}

templatelist=list(template) #convert to list
acc=0
while acc<10: #do 10 iterations
    acc+=1
    newlist=[] 
    for i in range(len(templatelist)-1):#first get a list of all the pairs
        twochars="".join(templatelist[i:i+2])
        newlist.append(mydict[twochars]) #append to newlist what the pair creates
    
    outlist=[]#Now create a new polymer be crossing the old and the new
    for i in range(len(templatelist+newlist)): #iterate over the amount of characters in the new polymer (length old + length new)
        if int(i) % 2 ==0: #if its even append from the old list
            outlist.append(templatelist[int(i/2)])
        else: #if its odd append from the new list
            outlist.append(newlist[(int((i-1)/2))])
    templatelist=outlist
    print("After step",acc,"length",len(templatelist),"".join(templatelist))

outdict=Counter(templatelist) #get counts
print("Final Answer:",max(outdict.values())-min(outdict.values())) #find max-min difference


#another way using a stack and iterating over the string directly
#developed this method when attempting to solve part 2

text_file = open("input.txt", "r")
lines = [v.strip("\n").split(" -> ") for v in text_file.readlines() if v !="\n"] #get all edges as a list of tuples

template_str=lines[0][0]
mydict={item[0]:item[1] for item in lines[1:]}

acc=0
while acc<10:
    acc+=1
    outstring=""
    for i,char in enumerate(template_str):
        if i >0:
            newchar=mydict["".join(template_str[i-1:i+1])]
            outstring+=newchar
        outstring+=template_str[i]
    template_str=outstring
    print(acc,len(outstring))

outdict=Counter(outstring) #get counts
print("Final Answer:",max(outdict.values())-min(outdict.values())) #find max-min difference
