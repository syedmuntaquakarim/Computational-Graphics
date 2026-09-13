import numpy as np
import matplotlib.pyplot as plt

# 1. Parameters
a = 1 
k = 7/4

# 2. Polar Domain
theta = np.linspace(0, 8 * np.pi, 1000)

# 3. Core Flower Equations
r = a * np.cos(7/4 * theta) + a * np.sin(3 * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)
p = r * np.cos(theta + np.pi)
q = r * np.sin(theta + np.pi)

# 4. Stem
s = np.linspace(0, -2, 200)
m = -s**2

# 5. Parametric Pointed Leaf (Positioned on the exposed stalk)
t = np.linspace(0, 2 * np.pi, 200)
L = 0.75   # Leaf length
W = 0.20   # Leaf width

# Sharp cusp profile
u = (L / 2) * (1 + np.cos(t))
v = W * np.sin(t)**3

# Anchor placed on the bare stalk below petals (s0 = -1.45 -> m0 = -2.10)
s0 = -1.45
m0 = -s0**2
phi = np.radians(20)  # Gentle upward-right tilt

# 2D rotation and translation
xl = s0 + (u * np.cos(phi) - v * np.sin(phi))
yl = m0 + (u * np.sin(phi) + v * np.cos(phi))

# Center leaf vein
u_vein = np.linspace(0, L, 50)
xl_vein = s0 + u_vein * np.cos(phi)
yl_vein = m0 + u_vein * np.sin(phi)

# Left Leaf (lower on the stem)
s1 = -1.7
m1 = -s1**2
phi_left = np.radians(155)  # Points up and left
L2, W2 = 0.65, 0.18

u2 = (L2 / 2) * (1 + np.cos(t))
v2 = W2 * np.sin(t)**3

xl2 = s1 + (u2 * np.cos(phi_left) - v2 * np.sin(phi_left))
yl2 = m1 + (u2 * np.sin(phi_left) + v2 * np.cos(phi_left))

# Optional central leaf vein
u_vein = np.linspace(0, L, 50)
xl_vein = s0 + u_vein * np.cos(phi)
yl_vein = m0 + u_vein * np.sin(phi)

# 6. Plot
plt.plot(x, y, color='pink', lw=1.2)
plt.plot(p, q, color='pink', lw=1.2)
plt.plot(s, m, color='forestgreen', lw=2)
plt.plot(xl, yl, color='forestgreen', lw=1.8)
plt.plot(xl_vein, yl_vein, color='forestgreen', lw=1, linestyle='--')

plt.axis('equal')
plt.axis('off')
plt.plot(xl2, yl2, color='forestgreen', lw=1.8)
plt.show()