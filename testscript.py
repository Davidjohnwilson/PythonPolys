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
            sys.stdout.write('\bF')
    if result:
        passedtests += 1
    totaltests += 1



#=====================================================
#Test suite 1 - validpoly
if verbose:
    print "---------------------------------------"
    print "Test suite 1 - validpoly              "

#Test 1: x+1 a valid polynomial
testnum += 1
poly = [1,1]
result = validpoly(poly)
testoutput(testnum,result)

#Test 2: x^2-1 a valid polynomial
testnum += 1
poly = [1,0,-1]
result = validpoly(poly)
testoutput(testnum, result)

#Test 3: Empty polynomial not a valid polynomial
testnum += 1
poly = []
result = not validpoly(poly)
testoutput(testnum, result)

#Test 4: 0 polynomial a valid polynomial
testnum += 1
poly = [0]
result = validpoly(poly)
testoutput(testnum, result)

#Test 5: non-list input
testnum += 1
poly = 1
result = not validpoly(poly)
testoutput(testnum, result)

#Test 6&7: non-integer coefficients
testnum += 1
poly = [1,2,3,4.543]
result = not validpoly(poly)
testoutput(testnum, result)

testnum += 1
poly = [1,'a',3,4]
result = not validpoly(poly)
testoutput(testnum, result)

#=====================================================
#Test suite 1 - evalpoly
if verbose:
    print "---------------------------------------"
    print "Test suite 2 - evalpoly              "

#Test 8: x+1 evaluated at 3
testnum += 1
poly = [1,1]
val = 3
result = (evalpoly(poly, val) == 4)
testoutput(testnum,result)

#Test : invalid polynomial
testnum += 1
poly = [1,2,'a',1]
val = 3
try:
    evalpoly(poly,val)
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
