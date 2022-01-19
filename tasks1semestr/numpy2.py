import numpy as np
a = np.arange(0,101)
print(a)
b = a[a % 2 != 0]
print(b)
c = np.arange(0, 101, 1) 
c[c%2==1] = -1     
print(c)
