f=open("input.txt","r")
indexrange = lambda a, b: range(a, b + 1)
count=0

for line in f:
    a, b = line.strip().split(",")
    a = set(indexrange(*map(int, a.split("-"))))
    b = set(indexrange(*map(int, b.split("-"))))
    if(len(a-b)==0 or len(b-a)==0):
        count+=1

for line in f:
    a, b = line.strip().split(",")
    a = set(indexrange(*map(int, a.split("-"))))
    b = set(indexrange(*map(int, b.split("-"))))
    if(len(a&b) > 0):
        count+=1

print(count)