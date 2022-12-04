f=open("sample.txt","r")
indexrange = lambda a, b: range(a, b + 1)
count=0

for line in f:
    a, b = line.strip().split(",")
    a = set(indexrange(*map(int, a.split("-"))))
    b = set(indexrange(*map(int, b.split("-"))))
    print(a&b)