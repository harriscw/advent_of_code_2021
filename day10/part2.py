#Read data 
text_file = open("input.txt", "r")
lines = [list(v.strip("\n")) for v in text_file.readlines()]

matching_dict={"]":"[",")":"(","}":"{",">":"<"}
inv_map = {v: k for k, v in matching_dict.items()} #helpful to invert this dictionary to calculate points
points_dict={")":1,"]":2,"}":3,">":4}
totalpoints=[]#want the middle value, so save each line's points into a list
for line in lines:
    outlist=[]
    incomplete=True #we want to ignore corrupted lines (part 1) and focus on incoplete lines
    for char in line: #so we are first rerunning part 1 code to identify corrupted lines, and ignore them to focus on incomplete ones
        if char not in matching_dict.keys(): #if the current character is an open paren, append it (you can always add an open paren)
            outlist.append(char)
        elif outlist[-1]==matching_dict[char]: #else if the character matches the last character is your open paren list, using a dictionary here for lookup is a helpful alternative to lots of if else
            del outlist[-1] #then remove the last character because it got closed
        else: #else if the current character doesn't add a new paren or close the latest open then its corrupted and we can ignore it
            incomplete=False
            break
    if incomplete==True: #We've identified incomplete lines, lets calculate points for them
        points=0
        print(line)
        print("Incomplete",outlist)
        completionlist=[inv_map[x] for x in outlist] #map incomplete line to the characters that complete it
        completionlist.reverse() #reverse it for point counting
        print(completionlist)
        for item in completionlist: #calculate points as defined by problem
            points=points*5 + points_dict[item]
        print(points)
        totalpoints+=[points]

totalpoints.sort() #I suppose the input will have an odd number of complete lines so theres always a middle value
i=divmod((len(totalpoints)/2), 1)[0] #so get the integer part of the list length/2
print(totalpoints,"\nFinal Answer:",totalpoints[int(i)])