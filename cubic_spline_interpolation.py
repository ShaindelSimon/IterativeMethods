import numpy as np
from scipy.interpolate import CubicSpline

# Sample data points
x = np.array([1.2, 1.3, 1.4, 1.5, 1.6])
y = np.array([-1.2, -2.3, -0.5, 0.89, 1.37])

# Create a natural cubic spline interpolator
cs = CubicSpline(x, y, bc_type='natural')

# Interpolate at a new point, for example, x = 2.5
x_new = 1.55
y_new = cs(x_new)

print(f"Interpolated value at x = {x_new}: y = {y_new}")