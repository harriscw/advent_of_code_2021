# Initially I tried to do this by iterating over each character, +1 for open, -1 for closed
# After some blatant cheating, I plagiarized the idea that the latest opened paren needs to be closed before the preceding ones
# This made things easy - if the current character is an open paren add it to the sequence of open parens
# If its a closed paren it needs to close the last open paren in your sequential list

#Read data 
text_file = open("input.txt", "r")
lines = [list(v.strip("\n")) for v in text_file.readlines()]

matching_dict={"]":"[",")":"(","}":"{",">":"<"}
points_dict={")":3,"]":57,"}":1197,">":25137}
points=0
for line in lines:
    print(line)
    outlist=[] #create a list of sequential open parens
    for char in line:
        print(outlist)
        if char not in matching_dict.keys(): #if the current character is an open paren, append it (you can always add an open paren)
            outlist.append(char)
        elif outlist[-1]==matching_dict[char]: #else if the character matches the last character is your open paren list, using a dictionary here for lookup is a helpful alternative to lots of if else
            del outlist[-1] #then remove the last character because it got closed
        else: #else if the current character doesn't add a new paren or close the latest open then its a mistake
            print("found one",char)
            points+=points_dict[char] # using a dictionary here for lookup is a helpful alternative to lots of if else
            break
print(points)