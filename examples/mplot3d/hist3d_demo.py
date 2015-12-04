"""
Creates a histogram for 2D data.
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y = np.random.rand(2, 100) * 4
# `z_hist` is a len(x) times len(y) array that contains the number of data
# points in each class.
z_hist, x_edges, y_edges = np.histogram2d(x, y, bins=4)

# Compute the position of all left bar edges
x_left, y_left = np.meshgrid(x_edges[:-1], y_edges[:-1], indexing='ij')
x_right, y_right = np.meshgrid(x_edges[1:], y_edges[1:], indexing='ij')

x_left = x_left.flatten()
y_left = y_left.flatten()
z_bottom = np.zeros_like(x_left)

x_right = 0.9 * x_right.flatten()
y_right = 0.9 * y_right.flatten()
z_top = z_hist.flatten()

ax.bar3d(x_left, y_left, z_bottom, x_right, y_right, z_top)

plt.show()
