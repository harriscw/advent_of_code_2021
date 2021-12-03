#Read data 
text_file = open("input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

def find_param(lines,spot,gamma=True): #function to find the most commonly occuring character in a given column
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
            return('0')
        else:
            return('1')
    else:
        if acc1>acc0:
            return('0')
        else:
            return('1')

gammastring=''
epsilonstring=''
for i in range(len(lines[0])): #iterate over each position to create a string of the most common character in each column
    gammastring+=find_param(lines,spot=i,gamma=True)
    epsilonstring+=find_param(lines,spot=i,gamma=False)

print("gamma:",gammastring,"\nepsilon:",epsilonstring,"\nFinal Answer:",int(gammastring,2)*int(epsilonstring,2))