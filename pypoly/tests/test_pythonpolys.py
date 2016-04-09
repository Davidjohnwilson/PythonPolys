from pythonpolys import *

# =============================
# Test suite 1: validpoly
# =============================

# Test: x+1 a valid polynomial
def test_validpoly_1():
	poly = [1,1]
	assert validpoly(poly)

# Test: x^2-1 a valid polynomial
def test_validpoly_2():
	poly = [1,0,-1]
	assert validpoly(poly)

# Test: Empty polynomial not a valid polynomial
def test_validpoly_3():
	poly = []
	assert not validpoly(poly)

# Test: 0 polynomial a valid polynomial
def test_validpoly_4():
	poly = [0]
	assert validpoly(poly)

# Test: non-list input
def test_validpoly_5():
	poly = 1
	assert not validpoly(poly)

# Test: non-integer coefficients
def test_validpoly_6():
	poly = [1,2,3,4.543]
	assert not validpoly(poly)

#Test: non-integer coefficients
def test_validpoly_7():
	poly = [1,'a',3,4]
	assert not validpoly(poly)

# =============================
# Test suite 2: evalpoly_basic
# =============================

# Test: x+1 evaluated at 3
def test_evalpoly_basic_1():
	poly = [1,1]
	val = 3
	assert evalpoly_basic(poly, val) == 4

#Test: x^2+2x+1 at 3
def test_evalpoly_basic_2():
	poly = [1,2,1]
	val = 3
	assert evalpoly_basic(poly, val) == 16

#Test: zero polynomial and 1
def test_evalpoly_basic_3():
	poly = [0]
	val = 3
	assert evalpoly_basic(poly, val) == 0

#Test: Bigger polynomial
def test_evalpoly_basic_4():
	poly = [-1,0,0,0,0,0,0,0,-6,1,1]
	val = 3
	assert evalpoly_basic(poly, val) == 39365

#Test: invalid polynomial
def test_evalpoly_basic_5():
	poly = [1,2,'a',1]
	val = 3
	try:
		evalpoly_basic(poly, val) == 4
	except Exception as e:
		assert e.message == 'Not a valid polynomial'

# =============================
# Test suite 3: evalpoly_horner
# =============================

# Test: x+1 evaluated at 3
def test_evalpoly_horner_1():
	poly = [1,1]
	val = 3
	assert evalpoly_horner(poly, val) == 4

#Test: x^2+2x+1 at 3
def test_evalpoly_horner_2():
	poly = [1,2,1]
	val = 3
	assert evalpoly_horner(poly, val) == 16

#Test: zero polynomial and 1
def test_evalpoly_horner_3():
	poly = [0]
	val = 3
	assert evalpoly_horner(poly, val) == 0

#Test: Bigger polynomial
def test_evalpoly_horner_4():
	poly = [-1,0,0,0,0,0,0,0,-6,1,1]
	val = 3
	assert evalpoly_horner(poly, val) == 39365

#Test: invalid polynomial
def test_evalpoly_horner_5():
	poly = [1,2,'a',1]
	val = 3
	try:
		evalpoly_horner(poly, val) == 4
	except Exception as e:
		assert e.message == 'Not a valid polynomial'



