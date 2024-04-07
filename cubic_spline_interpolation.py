import numpy as np
from scipy.interpolate import CubicSpline

# Sample data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])

# Create a cubic spline interpolator
cs = CubicSpline(x, y)

# Interpolate at a new point, for example, x = 2.5
x_new = 2.5
y_new = cs(x_new)

print(f"Interpolated value at x = {x_new}: y = {y_new}")
