
# coding: utf-8
from __future__ import division


#   Python Polynomial Module
#     by David John Wilson

# Implementation of polynomials in python
if __name__ == "__main__":
    print "---------------------------------------"
    print "Python Polynomial Module"
    print "Code by David John Wilson"
    print "Email: D.J.Wilson@bath.ac.uk"
    print "Last Updated: 24/08/2013"
    print "---------------------------------------"


# We need to import some important mathematical functions
from math import pow
from math import sqrt


# (Initially at least) we will consider a polynomial to be a list, P,
# where P[i] is the coefficient of x^i.

# validpoly
# Checks if a polynomial is valid for our module. Will be used as a
# first step error check in most functions.
# Input: testpoly - a polynomial to be tested for validity
# Output: True if a valid polynomial, False if not
# Example: validpoly([1,2,2]) => True
def validpoly(testpoly):
    if not type(testpoly) is list:
        return False
    if len(testpoly) == 0:
        return False
    for i in testpoly:
        if not type(i) is int:
            return False
    return True

# evalpoly_basic
# Evaluates a polynomial at a value.
# Input: poly - a polynomial to be evaluated
#        val  - the value to be evaluated at
# Output: True if a valid polynomial, False if not
# Example: evalpoly_basic([1,2,1], 3) => 16
def evalpoly_basic(poly,val):
    if not validpoly(poly):
        raise Exception('Not a valid polynomial')
    evaltot = 0
    for i in xrange(len(poly)):
        evaltot += poly[i] * (val**i)
    return evaltot

# evalpoly_horner
def evalpoly_horner(poly,val):
    if not validpoly(poly):
        raise Exception('Not a valid polynomial')
    polylen = len(poly)
    evaltot = poly[polylen-1]
    for i in xrange(1,polylen):
        evaltot = poly[polylen-(i+1)] + (evaltot * val)
    return evaltot

#evalpoly
#
def evalpoly(poly,val):
    return evalpoly_horner(poly,val)

#polydegree(poly)
def polydegree(poly):
    if not validpoly(poly):
        raise Exception('Not a valid polynomial')
    return (len(poly)-1)


#dispsqrt
def dispsqrt(argument):
    return "√"+'['+str(argument)+']'

#disproot
def disproot(power,argument):
    return "("+str(power)+")"+"√"+'['+str(argument)+']'

#solve_quad_symbolic
def solve_quad_symbolic(poly):
    if len(poly) != 3:
        raise Exception('Not a quadratic polynomial')
    discrim = pow(poly[1],2) - 4 * poly[0] * poly[2]
    if discrim == 0:
        if poly[1] % (2*poly[2]) == 0:
            term1 = poly[1]/(2*poly[2])
            return str(term1)
        else:
            return str(poly[1]) +'/'+ str(2*poly[2])
    if (poly[2] % (2*poly[2]) == 0) and (discrim % (4*poly[2]*poly[2]) == 0):
        term1 = poly[2] / (2*poly[2])
        term2 = discrim / (4*poly[2]*poly[2])
        return term1 + '±' + dispsqrt(term2)
    return '[' + str(-poly[1]) + '±' + dispsqrt(int(discrim)) +']' + '/' + str(2*poly[2])

print solve_quad_symbolic([5,7,1])

#solve_quad_numeric
def solve_quad_numeric(poly):
    if len(poly) != 3:
        raise Exception('Not a quadratic polynomial')
    discrim = pow(poly[1],2) - 4 * poly[0] * poly[2]
    if discrim == 0:
        return poly[1]/(2*poly[2])
    elif discrim > 0:
        sols = [(-poly[1] + sqrt(discrim))/(2*poly[2]), (-poly[1] - sqrt(discrim))/(2*poly[2]) ]
        return sols
    else:
        return "No Solutions"


print solve_quad_numeric([5,7,1])

#solve_cubic_numeric
def solve_cubic_numeric(poly):
    a = poly[3]
    b = poly[2]
    c = poly[1]
    d = poly[0]
    p = -b/(3*a)
    q = pow(p, 3) + ((b*c - 3*a*d)/(6*pow(a,2)))
    r = c/(3*a)
    x = pow(q + sqrt(pow(q,2)+pow((r-pow(p,2)), 1)), 1/3.0) + pow(q - sqrt(pow(q,2)+pow((r-pow(p,2)), 1)), 1/3.0)+p
    return x

print solve_cubic_numeric([-1,0,0,1])

#differentiate_poly
def differentiate_poly(poly):
    diffpoly=[]
    for i in xrange(1,len(poly)):
        diffpoly.append(i*poly[i])
    return diffpoly

print differentiate_poly([25,5,7,1,6])
print differentiate_poly(differentiate_poly([25,5,7,1,6]))

