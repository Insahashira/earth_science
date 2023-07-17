import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = np.full_like(x, 5)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
