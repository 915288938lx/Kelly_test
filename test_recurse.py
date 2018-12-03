def test():
    for i in range(10):
        yield i
import numpy as np


t = test()
print(np.array(list(t)))