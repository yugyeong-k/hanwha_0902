import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, '*:r')
plt.show()

