line="tQQGmnrMnJnGfmvrRRPCjlbljFBdjFCjTjnP"
first_half=[]
second_half=[]

index=len(line)//2
first_half.append(line[:index])
second_half.append(line[index:-1])

print(first_half)
print(second_half)

for i in range(len(first_half)):
    a=list(set(first_half[i]) & set(second_half[i]))
    
print(a)