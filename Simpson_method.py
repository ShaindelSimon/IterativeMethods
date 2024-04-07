import math
import numpy as np

import sympy as sp

from colors import bcolors
from sympy.utilities.lambdify import lambdify
x = sp.symbols('x')
def simpsons_rule(f, a, b, n):
    """
    Simpson's Rule for Numerical Integration and calculating the error estimate

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals (must be even).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """

    """if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")"""

    while n % 2 != 0:
        n = int(input("Number of subintervals (n) must be even for Simpson's Rule, enter again."))

    h = (b - a) / n
    fourth_diff = sp.diff(f, x, 4)  # Second derivative to the function that defined by 'x' for error estimate
    f = lambdify(x, f)
    integral = f(a) + f(b)  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= h / 3

    # Calculating the error estimate
    err = b  # estimated error for upper bound
    fourth_diff = lambdify(x, fourth_diff)
    Error = (1 / 180) * h ** 4 * (b - a) * fourth_diff(err)
    print("fourth derivative is: ", fourth_diff(1))
    print("The estimated error for err = ", err, " is: ", Error)

    return integral


if __name__ == '__main__':
    f = sp.exp(x ** 2)
    n = 4
    a=0
    b=1

    print( f" Division into n={n} sections ")
    integral = simpsons_rule(f, 0, 1, n)
    print(bcolors.OKBLUE, f"Numerical Integration of definite integral in range [{a},{b}] is {integral}", bcolors.ENDC)

