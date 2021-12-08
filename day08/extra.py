# For this I wanted to just continue and solve by for the positioning of each component given that I had all the components in each number
# Didn't know what to do with the components once I had them (make a picture?)
# So I just used them to reencode numbers even though that could have been done directly with my number:letters dictionary

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

def get_parts(numberdict):
    outdict=dict()
    outdict["top"]=list(set(list(numberdict[1])) ^ set(numberdict[7]))[0] #whats in 7 but not 1
    outdict["middle"]=list(set(list(numberdict[0])) ^ set(numberdict[8]))[0]
    outdict["lowerleft"]=list(set(list(numberdict[9])) ^ set(numberdict[8]))[0]
    outdict["upperright"]=list(set(list(numberdict[6])) ^ set(numberdict[8]))[0]
    outdict["lowerright"]=list(set(numberdict[1]) & set(numberdict[6]))[0]
    int14=list(set(list(numberdict[4])) ^ set(numberdict[1]))#in 4 but not 1 and not middle
    outdict["upperleft"]=list(filter(lambda int14: int14 !=outdict["middle"], int14))[0]
    outdict["bottom"]=list(set(['a','b','c','d','e','f','g']) ^ set(outdict.values()))[0]

    parts_to_num_dict = {k: v for k, v in sorted(outdict.items(), key=lambda x: x[1])}
    return(parts_to_num_dict)

num_to_parts_dict=dict()
num_to_parts_dict[0]=["top","upperright","lowerright","bottom","lowerleft","upperleft"]
num_to_parts_dict[1]=["upperright","lowerright"]
num_to_parts_dict[2]=["top","upperright","bottom","lowerleft","middle"]
num_to_parts_dict[3]=["top","upperright","lowerright","bottom","middle"]
num_to_parts_dict[4]=["upperright","lowerright","upperleft","middle"]
num_to_parts_dict[5]=["top","lowerright","bottom","upperleft","middle"]
num_to_parts_dict[6]=["top","lowerright","bottom","lowerleft","upperleft","middle"]
num_to_parts_dict[7]=["upperright","lowerright","top"]
num_to_parts_dict[8]=["top","upperright","lowerright","bottom","lowerleft","upperleft","middle"]
num_to_parts_dict[9]=["top","upperright","lowerright","bottom","upperleft","middle"]

def reencode(parts_to_num_dict,num_to_parts_dict,num):
    numlist=list(str(num))
    outlist=list()
    for item in numlist:
        outstring=""
        for thisnum in num_to_parts_dict[int(item)]:
            outstring+=parts_to_num_dict[thisnum]
        outlist.append(outstring)
    return(outlist)

def do_a_bunch(lines,num):
    for line in lines:
        numberdict=decode(line=line) #create a dictionary where key is a given number and value are the components (letter)
        parts_to_num_dict=get_parts(numberdict=numberdict) #create a dictionary where keys are locations of the 7 segment number display, values are components (letter)
        ret=reencode(parts_to_num_dict=parts_to_num_dict,num_to_parts_dict=num_to_parts_dict,num=num)#function to convert a number back to component letter using parts
        print(ret)
    return("")

print(do_a_bunch(lines=lines,num=11110191817152686282))
    