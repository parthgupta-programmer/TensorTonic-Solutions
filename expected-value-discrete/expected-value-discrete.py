import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    x=np.array(x)
    p=np.array(p)

    s=0.0
    
    for xi,pi in zip(x,p):
        s+=xi*pi

    return s