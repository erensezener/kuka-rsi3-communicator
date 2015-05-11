filename = 'temp.txt'

import numpy as np
import matplotlib.pyplot as plt
array = np.genfromtxt(filename)
plt.plot(array)
plt.show()
