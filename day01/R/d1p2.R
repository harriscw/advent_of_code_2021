text_file = as.numeric(unlist(read.table("../input.txt", header=FALSE)))

acc=0
for(i in 1:length(text_file)){#iterate over each number
  if(i <length(text_file)-2){ #stop when you run out of numbers
    prevsum=sum(text_file[(i):(i+2)]) #at each step get the sum of the 3 numbers ahead
    thissum=sum(text_file[(i+1):(i+3)]) #then go forward a step and get the sum of the 3 numbers ahead of that
    if(thissum>prevsum){ #if there's an increase then add 1
      acc=acc+1
    }
  }
}

print(paste("Final Answer:",acc))

