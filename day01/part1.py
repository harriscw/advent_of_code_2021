#Read data 
text_file = open("input.txt", "r")
lines = [int(v.strip("\n")) for v in text_file.readlines()]

acc=0
for i,num in enumerate(lines): #iterate over each number
    print(i,num)
    if i==0: #skip the first number b/c you cant compare it to the prior number
        continue
    else:
        if lines[i]>lines[i-1]: #if the number is more than the prior number then add 1
            acc+=1
print("Final Answer:",acc)