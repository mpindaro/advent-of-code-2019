import sys

with open(sys.argv[1], 'r') as f:
    input = f.read()
inputs=input.split("\n",1)
segments=[]

segments.append(inputs[0].split(",") )
segments.append(inputs[1].split(",") )

xs=[0,0]
ys=[0,0]
s=""

for i in range(0,len(segments)):
    wire=segments[i]
    for j in range(0, len(wire)):
        current=wire[j]
        direction=current[0]
        for v in range(1,len(current)):
            s+=current[v]
        offset=int(s)
        if direction == 'R':
            xs[i]+=offset
        elif direction == 'L':
            xs[i]-=offset
        elif direction == 'U':
            ys[i]+=offset
        else:
            ys[i]-=offset

        if i==0:
            print(xs[i], ":", ys[i], "\n")
