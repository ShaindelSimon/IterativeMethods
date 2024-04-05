##Shain Simon
def find_roots(f, a, b, step=0.1, tol=1e-6):
    """
    Find roots of function f within the interval [a, b]
    using a simple iterative method.
    """
    roots = []
    x = a
    while x <= b:
        if f(x) == 0:
            if not roots or abs(x - roots[-1]) > tol:
                roots.append(x)
                print(f"Root found: {x}")
        elif f(a) * f(x + step) < 0:
            x0, x1 = x, x + step
            iterations = 0
            while abs(x1 - x0) > tol:
                iterations += 1
                x0, x1 = x1, x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
                print(f"Iteration {iterations}: x({iterations+1}) = {x1}, f(x({iterations+1})) = {f(x1)}")
            if not roots or abs(x1 - roots[-1]) > tol:
                roots.append(x1)
                print(f"Root found: {x1}")
        x += step
    return roots

if __name__ == "__main__":
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5

    def func1(x):
        return (b*x**2 -e*x + b) / (d * x)

    def func2(x):
        return (b*x**2 +c*x**3 -d) / (c*x**2 -e)

    # Find all roots within the range from 0 to 3
    # f is not defined for zero
    roots = find_roots(func1, 0.00001, 3)
    print("\nFinal Roots 1:")
    for root in roots:
        print(root)

    print("\n")

    roots = find_roots(func2, 0, 3)
    print("\nFinal Roots 2:")
    for root in roots:
        print(root)