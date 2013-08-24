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

def validpoly(testpoly):
    if not type(testpoly) is list:
        return False
    if len(testpoly) == 0:
        return False
    for i in testpoly:
        if not type(i) is int:
            return False
    return True




