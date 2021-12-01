-- function to read data
-- stolen from here: https://stackoverflow.com/questions/11201262/how-to-read-data-from-a-file-in-lua
function lines_from(file)
    lines = {}
    for line in io.lines(file) do 
      lines[#lines + 1] = tonumber(line)
    end
    return lines
end

-- Read the data
  local file = '../input.txt'
  local lines = lines_from(file)

-- Function to convert bool to number
-- stolen from here: https://stackoverflow.com/questions/48230472/boolean-to-number-in-lua
  function bool_to_number(value)
    return value and 1 or 0
  end

  function sum(t)
    local sum = 0
    for k,v in pairs(t) do
        sum = sum + v
    end

    return sum
end

  acc=0
  for k,v in pairs(lines) do
    if k < #lines-2 then
        prevsum=lines[k]+lines[k+1]+lines[k+2]
        thissum=lines[k+1]+lines[k+2]+lines[k+3]
        acc=acc+bool_to_number(thissum>prevsum)
        
    end
    print(k,prevsum,thissum,acc)
  end

  print("Final Answer",acc)