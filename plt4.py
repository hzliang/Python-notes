import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

dt = list()
ipt = '/root/b'
for line in open(ipt):
    num = int(line)
    dt.append(num)

dt_np = np.array(dt)
print(dt_np)
plt.figure()
plt.hist(dt_np,bins=1000,range=(0,1000),label='s')
equal_zero =dt_np[dt_np<=2]
ttl = dt_np.size
ttl_ez = equal_zero.size
print(ttl_ez/ttl)
plt.show()