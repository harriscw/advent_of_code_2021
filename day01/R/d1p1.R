text_file = as.numeric(unlist(read.table("../input.txt", header=FALSE)))

acc=0
for(i in 1:length(text_file)){#iterate over each number
  if(i!=1){#skip the first number b/c you cant compare it to the prior number
    if(text_file[i]>text_file[i-1]){#if the number is more than the prior number then add 1
      acc=acc+1
    } 
  }
}

print(paste("Final Answer:",acc))
