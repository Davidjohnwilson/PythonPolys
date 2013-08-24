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

# evalpoly
# Input: poly - a polynomial to be evaluated
#        val  - the value to be evaluated at
# Output: True if a valid polynomial, False if not
# Example: evalpoly([1,2,1], 3) => 16
def evalpoly(poly,val):
    if not validpoly(poly):
        raise Exception('Not a valid polynomial')
    evaltot = 0
    for i in xrange(len(poly)):
        evaltot += poly[i] * (val**i)
    return evaltot

