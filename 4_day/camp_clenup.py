f=open("input.txt","r")
indexrange = lambda a, b: range(a, b + 1)

def p1(f):
    count=0
    for line in f:
        a, b = line.strip().split(",")
        a = set(indexrange(*map(int, a.split("-"))))
        b = set(indexrange(*map(int, b.split("-"))))
        if(len(a-b)==0 or len(b-a)==0):
            count+=1
    return count

def p2(f):
    count=0
    for line in f:
        a, b = line.strip().split(",")
        a = set(indexrange(*map(int, a.split("-"))))
        b = set(indexrange(*map(int, b.split("-"))))
        if(len(a&b) > 0):
            count+=1
    return count

print(p1(f))
print(p2(f))