import matplotlib.pyplot as plt
import numpy as np

a = 2
b = -4
c = 1

x = np.linspace(-5, 5, 400)
y = a*x**2 + b*x + c

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Parabola: y = 2x² - 4x + 1")
plt.grid(True)

plt.show()

