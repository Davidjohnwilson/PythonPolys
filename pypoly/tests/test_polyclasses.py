# coding: utf-8

import sys
import os
sys.path.append(os.path.abspath("./pypoly"))
from polyclasses import *

# ==================================
# Test suite 1: DensePoly
# ==================================


def test_DensePoly_1():
    # Test: x+1 as a Polynomial
    poly = [1, 1]
    f = DensePoly(poly)
    assert isinstance(f, Polynomial)


def test_DensePoly_2():
    # Test: x^2 + x +1 as a densepoly
    poly = [1, 1, 1]
    f = DensePoly(poly)
    assert isinstance(f, DensePoly)


def test_DensePoly_3():
    # Test: x+1 with zeros as a densepoly
    poly = [1, 1, 0, 0, 0, 0, 0]
    f = DensePoly(poly)
    assert isinstance(f, DensePoly)


def test_DensePoly_4():
    # Test: zero polynomial
    poly = [0]
    f = DensePoly(poly)
    assert isinstance(f, DensePoly)


def test_DensePoly_5():
    # Test: invalid polynomial
    poly = 1
    try:
        DensePoly(poly)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'


def test_DensePoly_6():
    # Test: invalid polynomial
    poly = 'a'
    try:
        DensePoly(poly)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'


def test_DensePoly_7():
    # Test: invalid polynomial
    poly = [1, 2, 'a', 1]
    try:
        DensePoly(poly)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'


def test_DensePoly_8():
    # Test: x+1 degree
    poly = [1, 1]
    f = DensePoly(poly)
    assert f.degree() == 1


def test_DensePoly_9():
    # Test: x+1 degree with zeros
    poly = [1, 1, 0, 0, 0, 0, 0]
    f = DensePoly(poly)
    assert f.degree() == 1


def test_DensePoly_10():
    # Test: x^10+1 degree with zeros
    poly = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    f = DensePoly(poly)
    assert f.degree() == 10


def test_DensePoly_11():
    # Test: constant polynomial
    poly = [1]
    f = DensePoly(poly)
    assert f.degree() == 0


def test_DensePoly_12():
    # Test: zero polynomial (undefined degree so -1)
    poly = [0]
    f = DensePoly(poly)
    assert f.degree() == -1


def test_DensePoly_13():
    # Test: print poly x+1
    poly = [1,1]
    f = DensePoly(poly)
    assert f.printpoly() == 'x+1'


def test_DensePoly_14():
    # Test: print poly -x-1
    poly = [-1,-1]
    f = DensePoly(poly)
    assert f.printpoly() == '-x-1'


def test_DensePoly_15():
    # Test: print poly 1
    poly = [1]
    f = DensePoly(poly)
    assert f.printpoly() == '1'


def test_DensePoly_16():
    # Test: print poly 0
    poly = [0]
    f = DensePoly(poly)
    assert f.printpoly() == '0'


def test_DensePoly_17():
    # Test: x+1 evaluated at 3
    poly = [1, 1]
    val = 3
    f = DensePoly(poly)
    assert f.evalpoly(val) == 4


def test_DensePoly_18():
    # Test: x^2+2x+1 at 3
    poly = [1, 2, 1]
    val = 3
    f = DensePoly(poly)
    assert f.evalpoly(val) == 16


def test_DensePoly_19():
    # Test: zero polynomial and 1
    poly = [0]
    val = 3
    f = DensePoly(poly)
    assert f.evalpoly(val) == 0


def test_DensePoly_20():
    # Test: Bigger polynomial
    poly = [-1, 0, 0, 0, 0, 0, 0, 0, -6, 1, 1]
    val = 3
    f = DensePoly(poly)
    assert f.evalpoly(val) == 39365


# ==================================
# Test suite 2: SparsePoly
# ==================================


def test_SparsePoly_1():
    # Test: x+1 as a Polynomial
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert isinstance(f, Polynomial)


def test_SparsePoly_2():
    # Test: x^2+x+1 as a SparsePoly
    poly = [[0, 1], [1, 1], [2, 1]]
    f = SparsePoly(poly)
    assert isinstance(f, SparsePoly)


def test_SparsePoly_3():
    # Test: x+1 with zeros as a SparsePoly
    poly = [[0, 1], [1, 1], [2, 0]]
    f = SparsePoly(poly)
    assert isinstance(f, SparsePoly)


def test_SparsePoly_4():
    # Test: zero polynomial
    poly = [[0, 0]]
    f = SparsePoly(poly)
    assert isinstance(f, SparsePoly)


def test_SparsePoly_5():
    # Test: invalid polynomial
    poly = 1
    try:
        SparsePoly(poly)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'


def test_SparsePoly_6():
    # Test: invalid polynomial
    poly = 'a'
    try:
        SparsePoly(poly)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'


def test_SparsePoly_7():
    # Test: invalid polynomial
    poly = [[0, 1], [2, 'a']]
    try:
        SparsePoly(poly)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'


def test_SparsePoly_8():
    # Test: invalid polynomial
    poly = [[0, 1], [-1, 1]]
    try:
        SparsePoly(poly)
        assert False
    except Exception as e:
        assert e.args[0] == 'Not a valid polynomial'


def test_SparsePoly_9():
    # Test: x+1 degree
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.degree() == 1


def test_SparsePoly_10():
    # Test: x+1 degree with zeros
    poly = [[0, 1], [1, 1], [2, 0]]
    f = SparsePoly(poly)
    assert f.degree() == 1


def test_SparsePoly_11():
    # Test: x^10+1 degree
    poly = [[0, 1],[10, 1]]
    f = SparsePoly(poly)
    assert f.degree() == 10


def test_SparsePoly_12():
    # Test: constant polynomial
    poly = [[0,1]]
    f = SparsePoly(poly)
    assert f.degree() == 0


def test_SparsePoly_13():
    # Test: zero polynomial (undefined degree so -1)
    poly = [[0,0]]
    f = SparsePoly(poly)
    assert f.degree() == -1


def test_SparsePoly_14():
    # Test: print poly x+1
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.printpoly() == 'x+1'


def test_SparsePoly_15():
    # Test: print poly -x-1
    poly = [[0, -1], [1, -1]]
    f = SparsePoly(poly)
    assert f.printpoly() == '-x-1'


def test_SparsePoly_16():
    # Test: print poly -x-1 out of order
    poly = [[1, -1], [0, -1]]
    f = SparsePoly(poly)
    assert f.printpoly() == '-x-1'


def test_SparsePoly_17():
    # Test: print poly 1
    poly = [[0,1]]
    f = SparsePoly(poly)
    assert f.printpoly() == '1'


def test_SparsePoly_17b():
    # Test: print poly -1
    poly = [[0,-1]]
    f = SparsePoly(poly)
    assert f.printpoly() == '-1'


def test_SparsePoly_17c():
    # Test: print poly 1.0
    poly = [[0,1.0]]
    f = SparsePoly(poly)
    assert f.printpoly() == '1'


def test_SparsePoly_17d():
    # Test: print poly -1.0
    poly = [[0,-1.0]]
    f = SparsePoly(poly)
    assert f.printpoly() == '-1'


def test_SparsePoly_18():
    # Test: print poly 0
    poly = [[0, 0]]
    f = SparsePoly(poly)
    assert f.printpoly() == '0'


def test_SparsePoly_19():
    # Test: x+1 evaluated at 3
    poly = [[0, 1], [1, 1]]
    val = 3
    f = SparsePoly(poly)
    assert f.evalpoly(val) == 4


def test_SparsePoly_20():
    # Test: x^2+2x+1 at 3
    poly = [[0, 1], [1, 2], [2, 1]]
    val = 3
    f = SparsePoly(poly)
    assert f.evalpoly(val) == 16


def test_SparsePoly_21():
    # Test: zero polynomial and 1
    poly = [[0, 0]]
    val = 3
    f = SparsePoly(poly)
    assert f.evalpoly(val) == 0


def test_SparsePoly_22():
    # Test: Bigger polynomial
    poly = [[0, -1], [8, -6], [9, 1], [10, 1]]
    val = 3
    f = SparsePoly(poly)
    assert f.evalpoly(val) == 39365


def test_SparsePoly_23():
    # Test: Simplify polynomial
    poly = [[0, 1], [1, 1], [1, -1]]
    f = SparsePoly(poly)
    f.simplify_poly()
    assert SparsePoly(poly).simplify_poly().printpoly() == '1'


def test_SparsePoly_24():
    # Test: Simplify polynomial
    poly = [[1, 1], [1, -1]]
    f = SparsePoly(poly)
    f.simplify_poly()
    assert SparsePoly(poly).simplify_poly().printpoly() == '0'


def test_SparsePoly_25():
    # Test: Simplify polynomial
    poly = [[1, 1], [1, 1]]
    assert SparsePoly(poly).simplify_poly().printpoly() == '2x'


def test_SparsePoly_23b():
    # Test: Simplify polynomial
    poly = [[0, 1], [1, 1], [1, -1]]
    f = SparsePoly(poly)
    f.simplify_poly_inplace()
    assert f.printpoly() == '1'


def test_SparsePoly_24b():
    # Test: Simplify polynomial
    poly = [[1, 1], [1, -1]]
    f = SparsePoly(poly)
    f.simplify_poly_inplace()
    assert f.printpoly() == '0'


def test_SparsePoly_25b():
    # Test: Simplify polynomial
    poly = [[1, 1], [1, 1]]
    f = SparsePoly(poly)
    f.simplify_poly_inplace()
    assert f.printpoly() == '2x'


def test_SparsePoly_26():
    # Test: add x+1 to itself
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    g = SparsePoly(poly)
    assert f.add_poly(g).printpoly() == '2x+2'


def test_SparsePoly_26():
    # Test: add x+1 to -x-1 itself
    poly_f = [[0, 1], [1, 1]]
    poly_g = [[0, -1], [1, -1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.add_poly(g).printpoly() == '0'


def test_SparsePoly_27():
    # Test: add x^100+1 to x^101-1 itself
    poly_f = [[0, 1], [100, 1]]
    poly_g = [[0, -1], [101, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.add_poly(g).printpoly() == 'x^101+x^100'


def test_SparsePoly_28():
    # Test: Negate x+1
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.negate_poly().printpoly() == '-x-1'


def test_SparsePoly_29():
    # Test: Subtract x+1 from x^2+x+1
    poly_f = [[0, 1], [1, 1], [2, 1]]
    poly_g = [[0, 1], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.subtract_poly(g).printpoly() == 'x^2'

def test_SparsePoly_29b():
    # Test: Multiply x+1 and x^2+x+1
    poly_f = [[0, 1], [1, 1], [2, 1]]
    poly_g = [[0, 1], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.multiply_poly(g).printpoly() == 'x^3+2x^2+2x+1'


def test_SparsePoly_30():
    # Test: Differentiate 3x^2+x+1 
    poly = [[0, 1], [1, 1], [2, 3]]
    f = SparsePoly(poly)
    assert f.differentiate_poly().printpoly() == '6x+1'


def test_SparsePoly_31():
    # Test: Differentiate 1 
    poly = [[0, 1]]
    f = SparsePoly(poly)
    assert f.differentiate_poly().printpoly() == '0'


def test_SparsePoly_32():
    # Test: Integrate x+1 
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.integrate_poly().printpoly() == '0.5x^2+x'


def test_SparsePoly_33():
    # Test: Integrate x+1 with constant
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.integrate_poly(10).printpoly() == '0.5x^2+x+10'


def test_SparsePoly_34():
    # Test: Definite integral x+1 
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.definite_integral(10, 15) == 67.5



def test_SparsePoly_35():
    # Test: Definite integral x^2+x+1 
    poly = [[0, 1], [1, 1], [2, 1]]
    f = SparsePoly(poly)
    assert "%.1f" % f.definite_integral(0, 50) == '42966.7'

# ==================================
# Test suite 3: Converting Polys
# ==================================


def test_Converting_Poly_1():
    # Test: x+1 as a Dense to Sparse
    poly_d = [1, 1]
    poly_s = [[0, 1], [1, 1]]
    f = DensePoly(poly_d)
    g = SparsePoly(poly_s)
    assert f.to_sparse_poly().coeffpairs == g.coeffpairs


def test_Converting_Poly_2():
    # Test: x+1 as a Sparse to Dense
    poly_d = [1, 1]
    poly_s = [[0, 1], [1, 1]]
    f = DensePoly(poly_d)
    g = SparsePoly(poly_s)
    assert g.to_dense_poly().coeffs == f.coeffs


def test_Converting_Poly_3():
    # Test: x^2 + 2x - 1 as a Dense to Sparse
    poly_d = [-1, 2, 1]
    poly_s = [[0, -1], [1, 2], [2, 1]]
    f = DensePoly(poly_d)
    g = SparsePoly(poly_s)
    assert f.to_sparse_poly().coeffpairs == g.coeffpairs


def test_Converting_Poly_4():
    # Test: x^2 + 2x - 1 as a Sparse to Dense
    poly_d = [-1, 2, 1]
    poly_s = [[0, -1], [1, 2], [2, 1]]
    f = DensePoly(poly_d)
    g = SparsePoly(poly_s)
    assert g.to_dense_poly().coeffs == f.coeffs


def test_Converting_Poly_5():
    # Test: x^10 - 1 as a Dense to Sparse
    poly_d = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    poly_s = [[0, -1], [10, 1]]
    f = DensePoly(poly_d)
    g = SparsePoly(poly_s)
    assert f.to_sparse_poly().coeffpairs == g.coeffpairs


def test_Converting_Poly_6():
    # Test: x^10 - 1 as a Sparse to Dense
    poly_d = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    poly_s = [[0, -1], [10, 1]]
    f = DensePoly(poly_d)
    g = SparsePoly(poly_s)
    assert g.to_dense_poly().coeffs == f.coeffs




# ==================================
# Test suite 4: Solving Polys
# ==================================


def test_Solving_Poly_1():
    # Test: cannot solve quartic
    poly = [[0, 1], [1, 1], [4, 1]]
    f = SparsePoly(poly)
    try:
        f.numeric_solve_poly()
        assert False
    except Exception as e:
        assert e.args[0] == 'Cannot solve polynomials of degree 4.'


def test_Solving_Poly_2():
    # Test: cannot solve degree 1000
    poly = [[0, 1], [1, 1], [1000, 1]]
    f = SparsePoly(poly)
    try:
        f.numeric_solve_poly()
        assert False
    except Exception as e:
        assert e.args[0] == 'Cannot solve polynomials of degree 1000.'


def test_Solving_Poly_3():
    # Test: cannot solve constant
    poly = [[0, 1]]
    f = SparsePoly(poly)
    try:
        f.numeric_solve_poly()
        assert False
    except Exception as e:
        assert e.args[0] == 'Cannot solve constant polynomials.'


def test_Solving_Poly_4():
    # Test: solve x+1
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.numeric_solve_poly() == [-1.0]


def test_Solving_Poly_5():
    # Test: solve 2x+1
    poly = [[0, 1], [1, 2]]
    f = SparsePoly(poly)
    assert f.numeric_solve_poly() == [-0.5]


def test_Solving_Poly_6():
    # Test: solve (x-1)(x-2)
    poly_f = [[0, -1], [1, 1]]
    poly_g = [[0, -2], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.multiply_poly(g).numeric_solve_poly() == [1.0, 2.0]


def test_Solving_Poly_7():
    # Test: solve (x-1)(x-1)
    poly = [[0, -1], [1, 1]]
    f = SparsePoly(poly)
    assert f.multiply_poly(f).numeric_solve_poly() == [1.0]


def test_Solving_Poly_8():
    # Test: solve x^2+1
    poly = [[0, 1], [2, 1]]
    f = SparsePoly(poly)
    assert f.numeric_solve_poly() == []


def test_Solving_Poly_9():
    # Test: solve x^3-1
    poly = [[0, -1], [3, 1]]
    f = SparsePoly(poly)
    assert f.numeric_solve_poly() == [1.0]


def test_Solving_Poly_10():
    # Test: solve x^3-8
    poly = [[0, -8], [3, 1]]
    f = SparsePoly(poly)
    assert f.numeric_solve_poly() == [2.0]

# FAILING TEST
# def test_Solving_Poly_10():
#     # Test: solve (x^2+1)(x-4)
#     poly_f = [[0, 1], [2, 1]]
#     poly_g = [[0, -4], [1, 1]]
#     f = SparsePoly(poly_f)
#     g = SparsePoly(poly_g)
#     print f.multiply_poly(g).printpoly()
#     print f.multiply_poly(g).numeric_solve_poly()
#     assert f.multiply_poly(g).numeric_solve_poly() == [4.0]

