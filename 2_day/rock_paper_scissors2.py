f=open("input.txt","r")  # open the file
count=0  # count the number of wines

for line in f:
    if line[2] == "X":
        count+=0
        if(line[0]=="A"):
            count+=3
        elif(line[0]=="B"):
            count+=1
        else:
            count+=2

    elif line[2] == "Y":
        count+=3
        if(line[0]=="A"):
            count+=1
        elif(line[0]=="B"):
            count+=2
        else:
            count+=3

        
    else:
        count+=6
        if(line[0]=="A"):
            count+=2
        elif(line[0]=="B"):
            count+=3
        else:
            count+=1
        


print(count)