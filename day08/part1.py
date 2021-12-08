#Read data 
text_file = open("input.txt", "r")
lines = [v.strip("\n").split(" | ") for v in text_file.readlines()]

print(lines)

#number of segments used
mydict={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}

#0 & 6 & 9 -> 6
#1 -> 2
#2 & 3 & 5 -> 5
#4 -> 4
#7 -> 3
#8 -> 7

acc=0
for line in lines:
    output=line[1].split(" ")
    for item in output:
        if len(item) in [2,4,3,7]:
            acc+=1
print(acc)