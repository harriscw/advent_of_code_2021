#Read data 
text_file = open("../input.txt", "r")
lines = [int(v.strip("\n")) for v in text_file.readlines()]

acc=0
for i,num in enumerate(lines): #iterate over each number
    if i <len(lines)-3: #stop when you run out of numbers
        prevsum=sum(lines[i:i+3]) #at each step get the sum of the 3 numbers ahead
        thissum=sum(lines[i+1:i+4]) #then go forward a step and get the sum of the 3 numbers ahead of that
        print(i,prevsum,thissum)
        if thissum>prevsum: #if there's an increase then add 1
            acc+=1
        
print('Final Answer:',acc)