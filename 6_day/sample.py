f=open("sample.txt","r")


def uniqueCharacters(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False;
    return True;


def p1(f):
    for l in f:
        count=[]
        j=0
        for i in range(4,len(l)):
            Mystr=l[j:i]
            j+=1
            if(uniqueCharacters(Mystr)):
                count.append(i)
    return count[0]


def p2(f):
    for l in f:
        count=[]
        j=0
        for i in range(14,len(l)):
            Mystr=l[j:i]
            j+=1
            if(uniqueCharacters(Mystr)):
                count.append(i)
    return count[0]


#print(p1(f))
print(p2(f))