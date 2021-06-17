import numpy as np 
import matplotlib.pyplot as plt

iterations = 1000
steps = 1000
plot_n = 5

dr = np.random.rand(steps, 2, iterations)*2 - 1
# array of (x, y) coordinates 
r = np.cumsum(dr, axis=0)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(r[:, 0, :plot_n], r[:, 1, :plot_n])
ax1.axis('square')

r2 = np.sum(np.average(r**2, axis=2), axis=1)
ax2.plot(r2)
# theoretical prediction is <r^2> = 2*N*<dx^2> = 2/3*N
ax2.plot(2/3*np.arange(1, steps+1, 1))
ax2.set(xlabel='Step', ylabel='Distance squared')

fig.tight_layout()
plt.show()