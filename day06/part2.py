#Read data 
text_file = open("input.txt", "r")
lines = list(map(int,[v.split(",") for v in text_file.readlines()][0]))

# After getting stumped with brute forcing deques and dictionaries this is the first day where I cheated a bit
# https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnhjkzl/?utm_source=share&utm_medium=web2x&context=3
# One area I get tripped up on is thinking "what computer science/programming approach am I missing" where a problem
# like this is just about thinking of different possible approaches

# The big idea here vs part 1 is no iterating over each element
# instead get counts, ie treat each "days until new fish" as a single group

thecounts=[lines.count(i) for i in range(0,8+1)] #get counts of unique days until new fish
print("day 0",thecounts)
acc=0
while acc<256: #iterate over days
    acc+=1
    if thecounts[0]!=0: #if the day is 0
        thecounts+=[thecounts[0]] #then add that many new fish
        thecounts[7]+=thecounts[0] #and set the parents' clock back
    else:
        thecounts+=[0] #otherwise no new fish
    del thecounts[0] #delete the fish who have had their clock set back, this then subtracts 1 from everyone
    print("day",acc,thecounts)

print("final answer:",sum(thecounts))
