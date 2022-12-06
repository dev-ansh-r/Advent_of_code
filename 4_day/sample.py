f=open("sample.txt","r")

def p1(f):
    count=0
    for line in f:
        a,b=line.strip().split(",")
        a0,a1=a.split('-')
        b0,b1=b.split('-')
        if int(a0)<=int(b0) and int(a1)>=int(b1):
            count+=1
        elif int(a0)>=int(b0) and int(a1)<=int(b1):
            count+=1
    return count

def p2(f):
    for line in f:
        count=0
        a,b=line.strip().split(",")
        a0,a1=a.split('-')
        b0,b1=b.split('-')
        if int(a0)<=int(b0) and int(a1)>=int(b1):
            count+=1
        elif int(a0)>=int(b0) and int(a1)<=int(b1):
            count+=1
    return count

print(p1(f))
