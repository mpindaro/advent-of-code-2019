import sys
import math
from functools import reduce

def fuelfuel(f,sum):
    if f<=0:
        return sum
    else:
        return fuelfuel(math.floor(f/3)-2,sum+f)

with open(sys.argv[1], 'r') as f:
    input = f.read()

fuels = list(map(lambda f: fuelfuel(math.floor(int(f)/3)-2,0) , input.split()))
fuel=reduce((lambda x, y: x + y), fuels)

print(fuel)
