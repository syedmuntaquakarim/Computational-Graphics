import numpy as np
import matplotlib.pyplot as plt

# 1. Parameters
a = 1 
k = 5

# 2. Polar Domain (1000 points from 0 to 2*pi)
theta = np.linspace(0, 2 * np.pi, 1000)

# 3. Core Equation
r = a * np.cos(k * theta)

# 4. Convert to Cartesian Coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# 5. Plot
# 5. Plot
plt.plot(x, y, color='cyan')
plt.axis('equal')
plt.axis('off')
plt.show()