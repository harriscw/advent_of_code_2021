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

  acc=0
  for k,v in pairs(lines) do
    if k ~= 1 then
        acc=acc+bool_to_number(lines[k]>lines[k-1])
    end
    print(k,v,acc)

  end

  print("Final Answer",acc)