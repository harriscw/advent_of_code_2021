#Read data 
text_file = open("../input.txt", "r")
lines = [v.strip("\n").split() for v in text_file.readlines()]

def p1():
    mydict = {"horizontal":0,"depth":0}
    for line in lines:
        if line[0]=="forward":
            mydict["horizontal"]+=int(line[1])
        elif line[0]=="down":
            mydict["depth"]+=int(line[1])
        elif line[0]=="up":
            mydict["depth"]-=int(line[1])

    print("Part 1:",mydict["horizontal"]*mydict["depth"])

def p2():
    mydict = {"horizontal":0,"depth":0,"aim":0}
    for line in lines:
        if line[0]=="forward":
            mydict["horizontal"]+=int(line[1])
            mydict["depth"]+=int(line[1])*mydict["aim"]
        elif line[0]=="down":
            mydict["aim"]+=int(line[1])
        elif line[0]=="up":
            mydict["aim"]-=int(line[1])

    print("Part 2:",mydict["horizontal"]*mydict["depth"])

p1()
p2()