import numpy as np
a = np.random.choice(np.arange(-1000, 1001), size=(50), replace=False)
print(a)
a=a[::-1]
print(a)
