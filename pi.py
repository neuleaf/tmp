import numpy as np
import random
import math

cnt=0
total=100000
for i in range(total):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    r=math.sqrt(x*x+y*y)
    if r<1.0:
        cnt+=1

print("Pi is {}.".format(4.0*cnt/total))