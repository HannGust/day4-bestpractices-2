"""
A collection of simple math operations
"""

def simple_add(a,b):
    """Adds two numbers together."""
    return a+b

def simple_sub(a,b):
    """Subtracts the second number from the first."""
    return a-b

def simple_mult(a,b):
    """Multiplies two numbers together."""
    return a*b

def simple_div(a,b):
    """Divides a number with another."""
    return a/b

def poly_first(x, a0, a1):
    """Evaluates a first order polynomial

    Evaluates the first order polynomial P(t) = a0 + a1 * t 
    at the point t = x. I.e. evaluates the expression a0 + a1 * x.

    Parameters
    ----------
    x : int or float
        The point at which to evalulate the polynomial.
    a0: int or float
        The constant coefficient of the polynomial, i.e. in the degree 0 term.
    a1: int or float
        The linear coefficient of the polynomial, i.e. in the degree 1 term.


    Returns
    -------
    int or float
        The value of the specified polynomial at the given point.

    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """Evaluates a second order polynomial

    Evaluates the second order polynomial P(t) = a0 + a1 * t + a2 * t**2
    at the point t = x. I.e. evaluates the expression a0 + a1 * x + a2 * x**2.

    Parameters
    ----------
    x : int or float
        The point at which to evalulate the polynomial.
    a0: int or float
        The constant coefficient of the polynomial, i.e. in the degree 0 term.
    a1: int or float
        The linear coefficient of the polynomial, i.e. in the degree 1 term.
    a2: int or float
        The quadratic coefficient of the polynomial, i.e. in the degree 2 term.


    Returns
    -------
    int or float
        The value of the specified polynomial at the given point.
    """

    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
