import numpy as np
def f1_micro(y_true, y_pred) -> float:
    y_true=np.asarray(y_true)
    y_pred=np.asarray(y_pred)

    tp=np.sum(y_true==y_pred)
    fp=np.sum(y_true != y_pred)
    fn=fp
    return (2 * tp) / (2 * tp + fp + fn)
    # 2*(P*R)/(P+R) = 2*((TP/(TP+FP))*(TP/(TP+FN))