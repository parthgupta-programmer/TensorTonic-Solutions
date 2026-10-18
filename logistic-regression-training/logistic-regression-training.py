import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    X=np.asarray(X,float)
    y=np.asarray(y,float)
    
    n,d=X.shape
    w=np.zeros(d)
    b=0.0

    for _ in range(steps):
        logits=X@w+b
        predictions=_sigmoid(logits)
        
        grad_w=X.T@(predictions-y)/n
        grad_b=np.mean(predictions-y)
        
        w-=lr*grad_w
        b-=lr*grad_b
        
    return w, b
        
        
    