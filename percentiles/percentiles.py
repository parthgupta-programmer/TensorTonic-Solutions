import numpy as np

def percentiles(x, q):
    x = sorted(x) 
    ans = []
    n = len(x)
    for qi in q:
        l = (qi / 100) * (n - 1)
        l1 = int(l)
        u = l1 + 1       
        if u >= n:     
            ans.append(x[l1])
        else:
            ans.append(x[l1] + (l - l1) * (x[u] - x[l1]))
    return np.array(ans)