import math
import numpy as np
from colors import bcolors

"""
Performs Iterative methods for Nonlinear Systems of Equations to determine the roots of the given function f
Receives 4 parameters:
    1. f - continuous function on the interval [a, b], where f (a) and f (b) have opposite signs.
    2. a - start value.
    3. b - end  value. 
    4. tol - the tolerable error , the default value will set as 1e-16

Returns variables:
    1.  c - The approximate root of the function f
"""
def bisection_method(f, a, b, tol=1e-6):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")
    c, k = 0, 0
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Iteration", "a", "b", "f(a)", "f(b)", "c", "f(c)"))

    # while the diff af a&b is not smaller than tol, and k is not greater than the max possible steps
    while abs(b - a) > tol:
        c = a + (b - a) / 2  # Calculation of the middle value
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(k, a, b, f(a), f(b), c, f(c)))

        if f(c) == 0 :
            return c  # Procedure completed successfully

        if f(c) * f(a) < 0:  # if sign changed between steps
            b = c  # move forward
        else:
            a = c  # move backward

        k += 1

    return c  # return the current root


if __name__ == '__main__':
    b = 3.75806452
    c = 0.91935484
    d = 5.5
    e = 6
    f = lambda x: (b*x**2 +c*x**3 -d) / (c*x**2 -e)
    roots = bisection_method(f, 0, 3, 0.0001)
    print(bcolors.OKBLUE, f"\nThe equation f(x) has an approximate root at x = {roots}",bcolors.ENDC,)

    # root_using_simple = simple_iterative(f, 0.1, 0.01, 10)
    # print(bcolors.OKBLUE, f"\nThe equation f(x) has an approximate root using simple iterative at x = {simple_iterative()}",bcolors.ENDC,)
