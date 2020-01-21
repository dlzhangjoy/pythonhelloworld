import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
plt.plot(x,y,'b')
plt.plot(x,y,'g',lw=5)
plt.show()