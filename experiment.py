import numpy as np
import matplotlib.pyplot as plt

# 1. Parameters
a = 1 
k = 7/4

# 2. Polar Domain (1000 points from 0 to 2*pi) theta = np.linspace(0, 8 * np.pi, 10000)
theta = np.linspace(0, 8 * np.pi, 1000)

# 3. Core Equation
r = a * np.cos(7/4 * theta) + a * np.sin(3 * theta)

# 4. Convert to Cartesian Coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# additional exp
p = r * np.cos(theta+np.pi)
q = r * np.sin(theta+np.pi)
s = np.linspace(0,-2)
m = -s**2
h = np.cos(theta)*np.sin(theta) + 3
g = np.cos(theta)*np.cos(theta) + 3


# 5. Plot
for i in range(16):
    for j in range(16):
        plt.plot(g-i,h-j ,color='yellow')
plt.plot(x, y, color='pink')
plt.plot(p, q, color='pink')
plt.plot(s,m, color='green')

plt.axis('equal')
plt.axis('off')
plt.show()

