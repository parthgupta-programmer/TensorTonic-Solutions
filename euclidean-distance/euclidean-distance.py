import numpy as np
import math

def euclidean_distance(x: list, y: list) -> float:
    x=np.array(x)
    y=np.array(y)

    s=0.0
    
    for xi,yi in zip(x,y):
        s+=(xi-yi)**2

    return math.sqrt(s)