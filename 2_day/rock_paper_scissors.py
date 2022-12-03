f=open("input.txt","r")  # open the file

count=0  # count the number of wines

for line in f:
    if line[2] == "X":
        count+=1
        #lose
    elif line[2] == "Y":
        count+=2
        #draw
    else :
        count+=3
        #win

    if(line[0] == "A" and line[2] == "X") or (line[0] == "B" and line[2] == "Y") or (line[0] == "C" and line[2] == "Z"):
        count+=3 #for draw match

    elif(line[0] == "A" and line[2] == "Y") or (line[0] == "B" and line[2] == "Z") or (line[0] == "C" and line[2] == "X"):
        count+=6 #for win match

print(count)