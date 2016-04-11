# coding: utf-8

import sys
import os
sys.path.append(os.path.abspath("./pypoly"))
from pythonpolys import *

# ==================================
# Test suite 1: validpoly
# ==================================


def test_validpoly_1():
    # Test: x+1 a valid polynomial
    poly = [1, 1]
    assert validpoly(poly)


def test_validpoly_2():
    # Test: x^2-1 a valid polynomial
    poly = [1, 0, -1]
    assert validpoly(poly)


def test_validpoly_3():
    # Test: Empty polynomial not a valid polynomial
    poly = []
    assert not validpoly(poly)


def test_validpoly_4():
    # Test: 0 polynomial a valid polynomial
    poly = [0]
    assert validpoly(poly)


def test_validpoly_5():
    # Test: non-list input
    poly = 1
    assert not validpoly(poly)


def test_validpoly_6():
    # Test: non-integer coefficients
    poly = [1, 2, 3, 4.543]
    assert not validpoly(poly)


def test_validpoly_7():
    # Test: non-integer coefficients
    poly = [1, 'a', 3, 4]
    assert not validpoly(poly)

# ==================================
# Test suite 2: disppoly (TODO)
# ==================================


# ==================================
# Test suite 3: evalpoly_basic
# ==================================


def test_evalpoly_basic_1():
    # Test: x+1 evaluated at 3
    poly = [1, 1]
    val = 3
    assert evalpoly_basic(poly, val) == 4


def test_evalpoly_basic_2():
    # Test: x^2+2x+1 at 3
    poly = [1, 2, 1]
    val = 3
    assert evalpoly_basic(poly, val) == 16


def test_evalpoly_basic_3():
    # Test: zero polynomial and 1
    poly = [0]
    val = 3
    assert evalpoly_basic(poly, val) == 0


def test_evalpoly_basic_4():
    # Test: Bigger polynomial
    poly = [-1, 0, 0, 0, 0, 0, 0, 0, -6, 1, 1]
    val = 3
    assert evalpoly_basic(poly, val) == 39365


def test_evalpoly_basic_5():
    # Test: invalid polynomial
    poly = [1, 2, 'a', 1]
    val = 3
    try:
        evalpoly_basic(poly, val)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'

# ==================================
# Test suite 4: evalpoly_horner
# ==================================


def test_evalpoly_horner_1():
    # Test: x+1 evaluated at 3
    poly = [1, 1]
    val = 3
    assert evalpoly_horner(poly, val) == 4


def test_evalpoly_horner_2():
    # Test: x^2+2x+1 at 3
    poly = [1, 2, 1]
    val = 3
    assert evalpoly_horner(poly, val) == 16


def test_evalpoly_horner_3():
    # Test: zero polynomial and 1
    poly = [0]
    val = 3
    assert evalpoly_horner(poly, val) == 0


def test_evalpoly_horner_4():
    # Test: Bigger polynomial
    poly = [-1, 0, 0, 0, 0, 0, 0, 0, -6, 1, 1]
    val = 3
    assert evalpoly_horner(poly, val) == 39365


def test_evalpoly_horner_5():
    # Test: invalid polynomial
    poly = [1, 2, 'a', 1]
    val = 3
    try:
        evalpoly_horner(poly, val)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'

# ==================================
# Test suite 5: evalpoly
# ==================================


def test_evalpoly_1():
    # Test: x+1 evaluated at 3
    poly = [1, 1]
    val = 3
    assert evalpoly(poly, val) == 4


def test_evalpoly_2():
    # Test: x^2+2x+1 at 3
    poly = [1, 2, 1]
    val = 3
    assert evalpoly(poly, val) == 16


def test_evalpoly_3():
    # Test: zero polynomial and 1
    poly = [0]
    val = 3
    assert evalpoly(poly, val) == 0


def test_evalpoly_4():
    # Test: Bigger polynomial
    poly = [-1, 0, 0, 0, 0, 0, 0, 0, -6, 1, 1]
    val = 3
    assert evalpoly(poly, val) == 39365


def test_evalpoly_5():
    # Test: invalid polynomial
    poly = [1, 2, 'a', 1]
    val = 3
    try:
        evalpoly(poly, val)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'

# ==================================
# Test suite 6: polydegree
# ==================================


def test_polydegree_1():
    # Test: x+1 evaluated at 3
    poly = [1, 1]
    assert polydegree(poly) == 1


def test_polydegree_horner_2():
    # Test: x^2+2x+1 at 3
    poly = [1, 2, 1]
    assert polydegree(poly) == 2


def test_polydegree_3():
    # Test: zero polynomial and 1
    poly = [0]
    assert polydegree(poly) == 0


def test_polydegree_4():
    # Test: Bigger polynomial
    poly = [-1, 0, 0, 0, 0, 0, 0, 0, -6, 1, 1]
    assert polydegree(poly) == 10


def test_polydegree_5():
    # Test: invalid polynomial
    poly = [1, 2, 'a', 1]
    try:
        polydegree(poly)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'

# ==================================
# Test suite 7: dispsqrt
# ==================================


def test_dispsqrt_1():
    # Test: dispsqrt of a integer
    arg = 3
    assert dispsqrt(arg) == "√[3]"


def test_dispsqrt_2():
    # Test: dispsqrt of a float
    arg = 1.23456789
    assert dispsqrt(arg) == "√[1.23456789]"


def test_dispsqrt_3():
    # Test: dispsqrt of a string
    arg = 'abc'
    assert dispsqrt(arg) == "√[abc]"


def test_dispsqrt_4():
    # Test: dispsqrt of an empty string
    arg = ''
    assert dispsqrt(arg) == "√[]"


def test_dispsqrt_5():
    # Test: dispsqrt of an array
    arg = [1, 2, 3]
    try:
        dispsqrt(arg)
        assert False
    except Exception as e:
        assert e.args[0] == 'Argument not a string or number'

# ==================================
# Test suite 8: disproot
# ==================================


def test_disproot_1():
    # Test: disproot of a number
    power = 2
    arg = 3
    assert disproot(power, arg) == "(2)√[3]"


def test_disproot_2():
    # Test: disproot of a float
    power = 1.23456789
    arg = 9.87654321
    assert disproot(power, arg) == "(1.23456789)√[9.87654321]"


def test_disproot_3():
    # Test: disproot of a string
    power = 'xyz'
    arg = 'abc'
    assert disproot(power, arg) == "(xyz)√[abc]"


def test_disproot_4():
    # Test: disproot of empty strings
    power = ''
    arg = ''
    assert disproot(power, arg) == "()√[]"


def test_disproot_5():
    # Test: disproot of an array (power)
    power = [1, 2, 3]
    arg = 5
    try:
        disproot(power, arg)
        assert False
    except Exception as e:
        assert e.args[0] == 'Power not a string or number'


def test_disproot_6():
    # Test: disproot of an array (argument)
    power = 1
    arg = [1, 2, 3]
    try:
        disproot(power, arg)
        assert False
    except Exception as e:
        assert e.args[0] == 'Argument not a string or number'


def test_disproot_7():
    # Test: disproot of an array (both)
    power = [1, 2, 3]
    arg = [1, 2, 3]
    try:
        disproot(power, arg)
        assert False
    except Exception as e:
        assert e.args[0] == 'Power not a string or number'

# ==================================
# Test suite 9: solve_quad_symbolic
# ==================================


def test_solve_quad_symbolic_1():
    # Test: solve quad symbolic
    poly = [5, 7, 1]
    assert solve_quad_symbolic(poly) == "[-7±√[29]]/2"


def test_solve_quad_symbolic_2():
    # Test: solve quad symbolic
    poly = [15, -8, 1]
    assert solve_quad_symbolic(poly) == "[8±√[4]]/2"


def test_solve_quad_symbolic_3():
    # Test: solve quad symbolic - discriminant zero
    poly = [2, 4, 2]
    assert solve_quad_symbolic(poly) == "1"


def test_solve_quad_symbolic_4():
    # Test: solve quad symbolic - negative discriminant
    poly = [2, 4, 4]
    assert solve_quad_symbolic(poly) == "[-4±√[-16]]/8"

# ==================================
# Test suite 10: solve_quad_numeric
# ==================================


def test_solve_quad_numeric_1():
    # Test: solve quad numeric
    poly = [5, 7, 1]
    assert solve_quad_numeric(poly) == [-0.8074175964327481,
                                        -6.192582403567252]


def test_solve_quad_numeric_2():
    # Test: solve quad numeric
    poly = [15, -8, 1]
    assert solve_quad_numeric(poly) == [5.0, 3.0]


def test_solve_quad_numeric_3():
    # Test: solve quad numeric - discriminant zero
    poly = [2, 4, 2]
    assert solve_quad_numeric(poly) == 1.0


def test_solve_quad_numeric_4():
    # Test: solve quad numeric - negative discriminant
    poly = [2, 4, 4]
    assert solve_quad_numeric(poly) == "No Solutions"

# ==================================
# Test suite 11: solve_cubic_numeric
# ==================================


def test_solve_cubic_numeric_1():
    # Test: solve cubic numeric
    poly = [-1, 0, 0, 1]
    assert solve_cubic_numeric(poly) == 1.0

# TODO - imaginary domain!
# # Test: solve cubic numeric
# def test_solve_cubic_numeric_2():
# 	poly = [-6,11,-6,1]
# 	assert solve_cubic_numeric(poly) == [1.0]
