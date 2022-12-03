f=open("input.txt","r")  # open the file
priorities = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44,  'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
data=f.read().split("\n")

first_half=[]
second_half=[]
priority=[]
total_sum=0

# read the file line by line and separate strimgs into two lists
for line in f:
    index=len(line)//2
    first_half.append(line[:index])
    second_half.append(line[index:-1])
for i in range(len(first_half)):
    priority.append("".join(set(first_half[i]) & set(second_half[i]))) 
for i in priority:
    total_sum += priorities.get(i)

#print(total_sum)
tmp=[]
value=[]
grand_total=0
for i in range(0,len(data),3):
    tmp.append(data[i:i+3])

for i in range(0,100):
    value.append("".join(set(tmp[i][0]) & set(tmp[i][1]) & set(tmp[i][2])))

for i in value:
    grand_total += priorities.get(i)

print(grand_total)
    