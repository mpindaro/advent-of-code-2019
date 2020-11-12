import sys
import math
from functools import reduce

with open(sys.argv[1], 'r') as f:
    input = f.read()
fuels = list(map(lambda x: math.floor(int(x)/3)-2 , input.split()))
fuel=reduce((lambda x, y: x + y), fuels)
print(fuel)
