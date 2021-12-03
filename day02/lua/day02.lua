-- stolen from here: https://stackoverflow.com/questions/11201262/how-to-read-data-from-a-file-in-lua
function lines_from(file)
    lines = {}
    for line in io.lines(file) do 
      lines[#lines + 1] = line
    end
    return lines
end

-- Stolen from here: https://stackoverflow.com/questions/1426954/split-string-in-lua
function mysplit (inputstr, sep)
    if sep == nil then
            sep = "%s"
    end
    local t={}
    for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
            table.insert(t, str)
    end
    return t
end

-- Read the data
local file = '../input.txt'
local lines = lines_from(file)
  
function p1 (lines)
    local horizontal = 0
    local depth = 0

    for k,v in pairs(lines) do
        instrux=mysplit(v," ")[1]
        thenum=tonumber(mysplit(v," ")[2])
        -- print(k,instrux,thenum)
        if instrux == "forward" then
            horizontal=horizontal+thenum
        elseif instrux == "down" then
            depth = depth+thenum
        elseif instrux == "up" then
            depth = depth-thenum
        end
    end
    print("Final Answer:",horizontal*depth)
end

function p2 (lines)
    local horizontal = 0
    local depth = 0
    local aim = 0

    for k,v in pairs(lines) do
        instrux=mysplit(v," ")[1]
        thenum=tonumber(mysplit(v," ")[2])
        -- print(k,instrux,thenum)
        if instrux == "forward" then
            horizontal=horizontal+thenum
            depth = depth+aim*thenum
        elseif instrux == "down" then
            aim = aim+thenum
        elseif instrux == "up" then
            aim = aim-thenum
        end
    end
    print("Final Answer:",horizontal*depth)
end

p1(lines)
p2(lines)

