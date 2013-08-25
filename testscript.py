# Testscript for Python Polynomial Module
#    by David John Wilson

if __name__ == "__main__":
    print "---------------------------------------"
    print "TestScript for Python Polynomial Module"
    print "Code by David John Wilson"
    print "Email: D.J.Wilson@bath.ac.uk"
    print "Last Updated: 24/08/2013"
    print "---------------------------------------"

# Import the polynomial module and all functions
from pythonpolys import *

# sys needed to parse command line arguments and write to stdout
import sys
# time needed for a pause function (mainly for debugging)
from time import sleep

if sys.argv[0] == 1:
    verbose = 1
    print "Verbose testing mode activated."
else:
    sys.stdout.write('Testing: ')
    verbose = 0

#Force verbosity
#verbose = 1

testnum = 0
passedtests = 0
totaltests = 0

def testoutput(testnum,result):
    global passedtests
    global totaltests
    if verbose:
        print "Test number " + str(testnum)
        strresult = "Passed" if result else "Failed"
        print "Result -> " + strresult
    else:
        sys.stdout.write('.')
        if result:
            #sleep(1.5)
            sys.stdout.write('\bP')
        else:
            sys.stdout.write('\bF('+str(testnum)+')')
    if result:
        passedtests += 1
    totaltests += 1



#=====================================================
#Test suite 1 - validpoly
if verbose:
    print "---------------------------------------"
    print "Test suite 1 - validpoly              "

#Test: x+1 a valid polynomial
testnum += 1
poly = [1,1]
result = validpoly(poly)
testoutput(testnum,result)

#Test: x^2-1 a valid polynomial
testnum += 1
poly = [1,0,-1]
result = validpoly(poly)
testoutput(testnum, result)

#Test: Empty polynomial not a valid polynomial
testnum += 1
poly = []
result = not validpoly(poly)
testoutput(testnum, result)

#Test: 0 polynomial a valid polynomial
testnum += 1
poly = [0]
result = validpoly(poly)
testoutput(testnum, result)

#Test: non-list input
testnum += 1
poly = 1
result = not validpoly(poly)
testoutput(testnum, result)

#Test: non-integer coefficients
testnum += 1
poly = [1,2,3,4.543]
result = not validpoly(poly)
testoutput(testnum, result)

#Test: non-integer coefficients
testnum += 1
poly = [1,'a',3,4]
result = not validpoly(poly)
testoutput(testnum, result)

#=====================================================
#Test suite 2 - evalpoly functions
if verbose:
    print "---------------------------------------"
    print "Test suite 2 - evalpoly functions      "

#evalpoly_basic
#Test: x+1 evaluated at 3
testnum += 1
poly = [1,1]
val = 3
result = (evalpoly_basic(poly, val) == 4)
testoutput(testnum,result)

#Test: x^2+2x+1 at 3
testnum += 1
poly = [1,2,1]
val = 3
result = (evalpoly_basic(poly, val) == 16)
testoutput(testnum,result)

#Test: zero polynomial and 1
testnum += 1
poly = [0]
val = 3
result = (evalpoly_basic(poly, val) == 0)
testoutput(testnum,result)

#Test: invalid polynomial
testnum += 1
poly = [1,2,'a',1]
val = 3
try:
    evalpoly_basic(poly,val)
    result = False
except:
    result = True
testoutput(testnum, result)

#evalpoly_horner
#Test: x+1 evaluated at 3
testnum += 1
poly = [1,1]
val = 3
result = (evalpoly_horner(poly, val) == 4)
testoutput(testnum,result)

#Test: x^2+2x+1 at 3
testnum += 1
poly = [1,2,1]
val = 3
result = (evalpoly_horner(poly, val) == 16)
testoutput(testnum,result)

#Test: zero polynomial and 1
testnum += 1
poly = [0]
val = 3
result = (evalpoly_horner(poly, val) == 0)
testoutput(testnum,result)

#Test: invalid polynomial
testnum += 1
poly = [1,2,'a',1]
val = 3
try:
    evalpoly_horner(poly,val)
    result = False
except:
    result = True
testoutput(testnum, result)

#=====================================================
# Final Results
#=====================================================
print ""
print "--------------  Results  -------------- "
print "Passed Tests: " + str(passedtests) + "/" + str(totaltests)
