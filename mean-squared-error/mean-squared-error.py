import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    y_pred=np.array(y_pred)
    y_true=np.array(y_true)

    s=0.0
    for y_predi,y_truei in zip(y_pred,y_true):
        s+=(y_predi-y_truei)**2
    return s/len(y_pred)
        