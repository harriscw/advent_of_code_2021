#Read data 
text_file = open("input.txt", "r")
lines = [v.strip("\n").split(" | ") for v in text_file.readlines()]

def decode(line): #This function decodes the input, sudoku logic style
    output=line[0].split(" ")
    output.sort(key=lambda s: len(s)) #Sort list based on length - super helpful!
    
    thisdict=dict()#create a dictionary where key is a given number and value are the components

    #The are gimmes
    thisdict[1]=list(output[0])
    thisdict[7]=list(output[1])
    thisdict[4]=list(output[2])
    thisdict[8]=list(output[9])

    #Look at length 6 components
    for checkthis in output[6:9]:
        intersection4=list(set(list(checkthis)) & set(thisdict[4]))
        intersection1=list(set(list(checkthis)) & set(thisdict[1]))
        if len(intersection4)==4: #if length of intersection with parts from 4 is 4 then its 9
            thisdict[9]=list(checkthis)
        elif len(intersection1)<2: #if length of intersection with parts from 1 < 2 then its 6
            thisdict[6]=list(checkthis)
        else:#else its 0
            thisdict[0]=list(checkthis)

    #Look at length 5 components
    for checkthis in output[3:6]:
        intersection1=list(set(list(checkthis)) & set(thisdict[1]))
        intersection6=list(set(list(checkthis)) & set(thisdict[6]))
        if len(intersection1)==2: #if length of intersection with parts from 1 is 2 then its 3
            thisdict[3]=list(checkthis)
        elif len(intersection6)==5: #if length of intersection with parts from 6 is 5 then its 5
            thisdict[5]=list(checkthis)
        else:#else its 2
            thisdict[2]=list(checkthis)
    return(thisdict)

def decipher(decodedict,thisnum): #this function deciphers an output given a dictionary where parts are known for each number
    for key in decodedict.keys(): #iterate over the keys in the dictionary
        theintersection=list(set(list(thisnum)) & set(decodedict[key])) #find the intersection with a given output number and the values at that key
        if len(theintersection)==len(list(thisnum)) and len(decodedict[key])==len(list(thisnum)): #if the length is the same and all the parts are there
            return(key) #spit out the decoded number

outlist=[]
for line in lines:#iterate line by line
    decodedict=decode(line) #create the dictionary where key is number and value is parts

    #now decode the output
    outnum=""
    for thisnum in line[1].split(" "): #iterate over each different encoded number in the output
        outnum=outnum+str(decipher(decodedict=decodedict,thisnum=thisnum)) #decipher and append to a string
    outlist.append(int(outnum)) #convert final string to int and append to list

print("Final Answer:",sum(outlist))