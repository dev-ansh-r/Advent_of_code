f=open("input.txt","r")
data = f.read().split("\n")
f.close()

elfs=[]

max_3=[] # list of elfs with max 3

total=0

for i in data:
    if i!="":
        total+=int(i)
    else:
        elfs.append(total)
        total=0

for i in range(0,3):
    max_3.append(max(elfs))
    elfs.remove(max(elfs))

print(sum(max_3))
