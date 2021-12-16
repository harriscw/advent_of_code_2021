#did a litle bit of cheating again here.
#got pretty frustrated playing with itertools and not getting anywhere
#so I peaked around reddit and saw a comment "this was like lanternfish part 2"
#from there I arrived at this solution

from collections import Counter
import itertools

text_file = open("input.txt", "r")
lines = [v.strip("\n").split(" -> ") for v in text_file.readlines() if v !="\n"]

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

template=lines[0][0] #original string
mydict={item[0]:item[1] for item in lines[1:]}#dictioary mapping pairs to new letters
lettercount=Counter(template)#dictioanry with frequency of letters in the original string
pairs=Counter(["".join(x) for x in list(pairwise(template))]) #dictionary with frequency of letter pairs in the original string

acc=0
while acc<40:
    acc+=1
    currentdict=dict(pairs) #make a copy of the pairs dictionary to retain original frequencies
    for key in currentdict.keys(): #iterate over keys
        # print(key,"adding",key[0]+mydict[key],mydict[key]+key[1],"freq",currentdict[key])
        if currentdict[key]>0: #only do something if that pair is in the current string
            lettercount[mydict[key]]+=currentdict[key] #update the letter count dictionary.  Increase by however many of the pair that map to that letter are in the original saved dictionary
            pairs[key[0]+mydict[key]]+=currentdict[key] #add one new pair to the pairs dictionary 
            pairs[mydict[key]+key[1]]+=currentdict[key] #add the other new pair to the pairs dictionary 
            pairs[key]-=currentdict[key] #The pair being iterated over is removed because letters have been inserted in between the pair.  So reduce by however many of the pair that map to that letter are in the original saved dictionary
    print("After Iteration",acc,"Length",sum(lettercount.values()))
    # print(lettercount)
    # print(pairs)

print("Final Answer:",max(lettercount.values())-min(lettercount.values()))