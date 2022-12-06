f=open("input.txt","r")

def p1(f):
    crates, instructions = f.read().split("\n\n")
    return crates,instructions

print(p1(f))