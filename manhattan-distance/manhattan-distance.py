import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    x=np.array(x)
    y=np.array(y)

    s=0.0
    
    for xi,yi in zip(x,y):
        s+=abs(xi-yi)
    return s