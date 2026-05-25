import numpy as np
import math
def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x=np.array(x)
    X1=1+np.exp(-x)
    return 1/X1
    pass