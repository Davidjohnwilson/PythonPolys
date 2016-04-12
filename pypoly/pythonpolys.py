# coding: utf-8
from __future__ import division

# We need to import some important mathematical functions
from math import pow
from math import sqrt

#   Python Polynomial Module
#     by David John Wilson

# Implementation of polynomials in python
if __name__ == "__main__":
    print("---------------------------------------")
    print("Python Polynomial Module               ")
    print("Code by David John Wilson              ")
    print("Email: D.J.Wilson@bath.ac.uk           ")
    print("Last Updated: 24/08/2013               ")
    print("---------------------------------------")

# (Initially at least) we will consider a polynomial to be a list, P,
# where P[i] is the coefficient of x^i.


def validpoly(testpoly):
    # validpoly
    # Checks if a polynomial is valid for our module. Will be used as a
    # first step error check in most functions.
    # Input: testpoly - a polynomial to be tested for validity
    # Output: True if a valid polynomial, False if not
    # Example: validpoly([1,2,2]) => True
    if not type(testpoly) is list:
        return False
    if len(testpoly) == 0:
        return False
    for i in testpoly:
        if not type(i) is int:
            return False
    return True


def disppoly(poly, variable='x'):
    # disppoly
    # Checks if a polynomial is valid for our module and if so
    # returns a human-readable string representation.
    # Input: poly - a polynomial to be printed
    #        variable - optional dummy variable (default: x)
    # Output: string representing the polynomial
    # Example: disppoly([1,2,2],'y') => '2y^2+2y+1'
    # TODO: negatives
    if not validpoly(poly):
        raise Exception('Not a valid polynomial')
    polyarr = []
    dummy_variable = str(variable)
    n = len(poly)
    if n == 0:
        return ''
    for i in range(1, n - 1):
        # we work backwards
        if poly[n - i] != 0 and poly[n - i] != 1 and poly[n - i] != -1:
            polyarr.append(str(poly[n - i]) +
                           dummy_variable + '^' + str(n - i))
        elif poly[n - i] == 1:
            polyarr.append(dummy_variable + '^' + str(n - i))
        elif poly[n - i] == -1:
            polyarr.append('-' + dummy_variable + '^' + str(n - i))
    if n > 0 and poly[1] != 0:
        if poly[1] == 1:
            polyarr.append(dummy_variable)
        elif poly[1] == -1:
            polyarr.append('-' + dummy_variable)
        else:
            polyarr.append(str(poly[1]) + dummy_variable)
    if poly[0] != 0:
        polyarr.append(str(poly[0]))
    return '+'.join(polyarr).replace('+-', '-')


def evalpoly_basic(poly, val):
    # evalpoly_basic
    # Evaluates a polynomial at a value.
    # Input: poly - a polynomial to be evaluated
    #        val  - the value to be evaluated at
    # Output: True if a valid polynomial, False if not
    # Example: evalpoly_basic([1,2,1], 3) => 16
    if not validpoly(poly):
        raise Exception('Not a valid polynomial')
    evaltot = 0
    for i in range(len(poly)):
        evaltot += poly[i] * (val ** i)
    return evaltot


def evalpoly_horner(poly, val):
    # evalpoly_horner
    if not validpoly(poly):
        raise Exception('Not a valid polynomial')
    polylen = len(poly)
    evaltot = poly[polylen - 1]
    for i in range(1, polylen):
        evaltot = poly[polylen - (i + 1)] + (evaltot * val)
    return evaltot


def evalpoly(poly, val, method='horner'):
    # evalpoly - defaults to horner
    if method == 'basic':
        return evalpoly_basic(poly, val)
    else:
        return evalpoly_horner(poly, val)


def polydegree(poly):
    # polydegree(poly)
    if not validpoly(poly):
        raise Exception('Not a valid polynomial')
    return (len(poly) - 1)


def dispsqrt(argument):
    # dispsqrt
    if not isinstance(argument, (int, float, str)):
        raise Exception('Argument not a string or number')
    return "√" + '[' + str(argument) + ']'


def disproot(power, argument):
    # disproot
    if not isinstance(power, (int, float, str)):
        raise Exception('Power not a string or number')
    if not isinstance(argument, (int, float, str)):
        raise Exception('Argument not a string or number')
    return "(" + str(power) + ")" + "√" + '[' + str(argument) + ']'


def solve_quad_symbolic(poly):
    # solve_quad_symbolic
    if len(poly) != 3:
        raise Exception('Not a quadratic polynomial')
    discrim = pow(poly[1], 2) - 4 * poly[0] * poly[2]
    if discrim == 0:
        if poly[1] % (2 * poly[2]) == 0:
            term1 = int(poly[1] / (2 * poly[2]))
            return str(term1)
        else:
            return str(poly[1]) + '/' + str(2 * poly[2])

    test_a = (poly[2] % (2 * poly[2]) == 0)
    test_b = (discrim % (4 * poly[2] * poly[2]) == 0)
    if test_a and test_b:
        term1 = poly[2] / (2 * poly[2])
        term2 = discrim / (4 * poly[2] * poly[2])
        return term1 + '±' + dispsqrt(term2)
    return '[' + str(-poly[1]) + '±' + dispsqrt(int(discrim)) + ']' + \
           '/' + str(2 * poly[2])

# print(solve_quad_symbolic([5, 7, 1]))


def solve_quad_numeric(poly):
    # solve_quad_numeric
    if len(poly) != 3:
        raise Exception('Not a quadratic polynomial')
    discrim = pow(poly[1], 2) - 4 * poly[0] * poly[2]
    if discrim == 0:
        return poly[1] / (2 * poly[2])
    elif discrim > 0:
        sols = [(-poly[1] + sqrt(discrim)) /
                (2 * poly[2]), (-poly[1] - sqrt(discrim)) / (2 * poly[2])]
        return sols
    else:
        return "No Solutions"


# print(solve_quad_numeric([5, 7, 1]))


def solve_cubic_numeric(poly):
    # solve_cubic_numeric
    a = poly[3]
    b = poly[2]
    c = poly[1]
    d = poly[0]
    p = -b / (3 * a)
    q = pow(p, 3) + ((b * c - 3 * a * d) / (6 * pow(a, 2)))
    r = c / (3 * a)
    x = pow(q + sqrt(pow(q, 2) + pow((r - pow(p, 2)), 1)), 1 / 3.0) + \
        pow(q - sqrt(pow(q, 2) + pow((r - pow(p, 2)), 1)), 1 / 3.0) + p
    return x

# print(solve_cubic_numeric([-1, 0, 0, 1]))


def differentiate_poly(poly):
    # differentiate_poly
    diffpoly = []
    n = len(poly)
    if n == 1:
        diffpoly = [0]
    for i in range(1, n):
        diffpoly.append(i * poly[i])
    return diffpoly

# print(differentiate_poly([25, 5, 7, 1, 6]))
# print(differentiate_poly(differentiate_poly([25, 5, 7, 1, 6])))
