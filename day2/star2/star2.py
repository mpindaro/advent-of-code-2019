import sys

with open(sys.argv[1], 'r') as f:
    input = f.read()

tokens=list(map(lambda x: int(x),input.split(",")))
tokenss=tokens
noun = 0
verb = 0
found=False
for noun in range(0,100):
    for verb in range(0,100):
        tokens=list(map(lambda x: int(x),input.split(",")))
        tokens[1]=noun
        tokens[2]=verb

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

        if tokens[0]==19690720:
            found=True
            break
    if found:
        break


print(noun*100+verb)
