import sympy as sp
from sympy.utilities.lambdify import lambdify

def Raphson(x, f, n1, n2, e=0.0001):
    df = sp.diff(f)
    f = lambdify(x, f)
    df = lambdify(x, df)

    X = (n1+n2)/2
    for i in range(100):
        next_X = X - f(X)/df(X)
        if abs(next_X - X) < e:
            print("number of iteration: ", i+1)
            return X
        if X > n2 or X < n1:
            raise Exception("out of range")
        X = next_X
    raise Exception("doesnt converge")

def Secant(f, n1, n2, e=0.0001):
    prev_X = n1 + 1/3 * (n2 - n1)
    X = n2 - 1/3 * (n2 - n1)
    for i in range(100):
        next_X = (prev_X * f(X) - X * f(prev_X)) / (f(X) - f(prev_X))
        if abs(next_X - X) < e:
            print("number of iteration: ", i+1)
            return X
        if X > n2 or X < n1:
            raise Exception("out of range")
        prev_X, X = X, next_X
    raise Exception("doesnt converge")


if __name__ == "__main__":
    X = sp.symbols("x")
    f = X**2-5*X+2

    print(Raphson(X, f, 0, 8))
    print(Secant(lambda X: X ** 2 - 5 * X + 2, -10, 5))