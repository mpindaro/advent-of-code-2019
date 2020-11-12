import sys

with open(sys.argv[1], 'r') as f:
    input = f.read()

tokens=list(map(lambda x: int(x),input.split(",")))
print(tokens)

tokens[1]=12
tokens[2]=2

for i in range(0,len(tokens),4):
    if tokens[i]==99:
        break
    elif tokens[i]==2:
        x=tokens[tokens[1+i]]
        y=tokens[tokens[2+i]]
        tokens[tokens[3+i]]=x*y
    else:
        x=tokens[tokens[1+i]]
        y=tokens[tokens[2+i]]
        tokens[tokens[3+i]]=x+y

print(tokens[0])
