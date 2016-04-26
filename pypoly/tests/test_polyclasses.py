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
    assert f.print_poly() == 'x+1'


def test_DensePoly_14():
    # Test: print poly -x-1
    poly = [-1,-1]
    f = DensePoly(poly)
    assert f.print_poly() == '-x-1'


def test_DensePoly_15():
    # Test: print poly 1
    poly = [1]
    f = DensePoly(poly)
    assert f.print_poly() == '1'


def test_DensePoly_16():
    # Test: print poly 0
    poly = [0]
    f = DensePoly(poly)
    assert f.print_poly() == '0'


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
    # Test: sorting coefficients 
    poly = [[1, 1], [0, 1]]
    f = SparsePoly(poly)
    assert f.coeffpairs == [[0, 1], [1, 1]]


def test_SparsePoly_10():
    # Test: combining coefficients 
    poly = [[1, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.coeffpairs == [[1, 2]]


def test_SparsePoly_11():
    # Test: lots of zero coefficients 
    poly = [[0, 0], [0, 0]]
    f = SparsePoly(poly)
    assert f.coeffpairs == [[0, 0]]


def test_SparsePoly_12():
    # Test: cancelling coefficients 
    poly = [[0, 1], [1, 1], [1, -1]]
    f = SparsePoly(poly)
    assert f.coeffpairs == [[0, 1]]


def test_SparsePoly_13():
    # Test: cancelling coefficients 
    poly = [[1, 1], [1, -1]]
    f = SparsePoly(poly)
    assert f.coeffpairs == [[0, 0]]

def test_SparsePoly_14():
    # Test: x+1 degree
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.degree() == 1


def test_SparsePoly_15():
    # Test: x+1 degree with zeros
    poly = [[0, 1], [1, 1], [2, 0]]
    f = SparsePoly(poly)
    assert f.degree() == 1


def test_SparsePoly_16():
    # Test: x^10+1 degree
    poly = [[0, 1],[10, 1]]
    f = SparsePoly(poly)
    assert f.degree() == 10


def test_SparsePoly_17():
    # Test: constant polynomial
    poly = [[0,1]]
    f = SparsePoly(poly)
    assert f.degree() == 0


def test_SparsePoly_18():
    # Test: zero polynomial (undefined degree so -1)
    poly = [[0,0]]
    f = SparsePoly(poly)
    assert f.degree() == -1


def test_SparsePoly_19():
    # Test: zero polynomial (undefined degree so -1) with extra zeros
    poly = [[0,0], [0, 0], [0, 0]]
    f = SparsePoly(poly)
    assert f.degree() == -1


def test_SparsePoly_20():
    # Test: print poly x+1
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.print_poly() == 'x+1'


def test_SparsePoly_21():
    # Test: print poly x+1
    poly = [[0, 1], [10, 1]]
    f = SparsePoly(poly)
    assert f.print_poly() == 'x^10+1'


def test_SparsePoly_22():
    # Test: print poly x+1
    poly = [[0, 1], [2, 1], [2, 1]]
    f = SparsePoly(poly)
    assert f.print_poly() == '2x^2+1'


def test_SparsePoly_23():
    # Test: print poly -x-1
    poly = [[0, -1], [1, -1]]
    f = SparsePoly(poly)
    assert f.print_poly() == '-x-1'


def test_SparsePoly_24():
    # Test: print poly -x-1 out of order
    poly = [[1, -1], [0, -1]]
    f = SparsePoly(poly)
    assert f.print_poly() == '-x-1'


def test_SparsePoly_25():
    # Test: print poly 1
    poly = [[0,1]]
    f = SparsePoly(poly)
    assert f.print_poly() == '1'


def test_SparsePoly_26():
    # Test: print poly -1
    poly = [[0,-1]]
    f = SparsePoly(poly)
    assert f.print_poly() == '-1'


def test_SparsePoly_27():
    # Test: print poly 1.0
    poly = [[0,1.0]]
    f = SparsePoly(poly)
    assert f.print_poly() == '1'


def test_SparsePoly_28():
    # Test: print poly -1.0
    poly = [[0,-1.0]]
    f = SparsePoly(poly)
    assert f.print_poly() == '-1'


def test_SparsePoly_29():
    # Test: print poly 0
    poly = [[0, 0]]
    f = SparsePoly(poly)
    assert f.print_poly() == '0'


def test_SparsePoly_30():
    # Test: print poly with non-integer coefficients
    poly = [[0, 1.6], [1, 2.3], [2, 182.948]]
    f = SparsePoly(poly)
    assert f.print_poly() == '182.948x^2+2.3x+1.6'


def test_SparsePoly_31():
    # Test: x+1 evaluated at 3
    poly = [[0, 1], [1, 1]]
    val = 3
    f = SparsePoly(poly)
    assert f.evalpoly(val) == 4


def test_SparsePoly_32():
    # Test: x^2+2x+1 at 3
    poly = [[0, 1], [1, 2], [2, 1]]
    val = 3
    f = SparsePoly(poly)
    assert f.evalpoly(val) == 16


def test_SparsePoly_33():
    # Test: x^2+2x+1 at float 1.5
    poly = [[0, 1], [1, 2], [2, 1]]
    val = 1.5
    f = SparsePoly(poly)
    assert f.evalpoly(val) == 6.25


def test_SparsePoly_34():
    # Test: zero polynomial and 1
    poly = [[0, 0]]
    val = 3
    f = SparsePoly(poly)
    assert f.evalpoly(val) == 0


def test_SparsePoly_35():
    # Test: Bigger polynomial
    poly = [[0, -1], [8, -6], [9, 1], [10, 1]]
    val = 3
    f = SparsePoly(poly)
    assert f.evalpoly(val) == 39365


def test_SparsePoly_36():
    # Test: Simplify polynomial
    poly = [[0, 1], [1, 1], [1, -1]]
    f = SparsePoly(poly)
    f.simplify_poly()
    assert f.coeffpairs == f.simplify_poly().coeffpairs


def test_SparsePoly_37():
    # Test: Simplify polynomial
    poly = [[1, 1], [1, -1]]
    f = SparsePoly(poly)
    f.simplify_poly()
    assert SparsePoly(poly).simplify_poly().print_poly() == '0'


def test_SparsePoly_38():
    # Test: Simplify polynomial
    poly = [[1, 1], [1, 1]]
    assert SparsePoly(poly).simplify_poly().print_poly() == '2x'


def test_SparsePoly_39():
    # Test: Simplify polynomial
    poly = [[0, 1], [1, 1], [1, -1]]
    f = SparsePoly(poly)
    f.simplify_poly_inplace()
    assert f.print_poly() == '1'


def test_SparsePoly_40():
    # Test: Simplify polynomial
    poly = [[1, 1], [1, -1]]
    f = SparsePoly(poly)
    f.simplify_poly_inplace()
    assert f.print_poly() == '0'


def test_SparsePoly_41():
    # Test: Simplify polynomial
    poly = [[1, 1], [1, 1]]
    f = SparsePoly(poly)
    f.simplify_poly_inplace()
    assert f.print_poly() == '2x'


def test_SparsePoly_42():
    # Test: Equal polynomial
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    g = SparsePoly(poly)
    assert f.equal_poly(g)


def test_SparsePoly_43():
    # Test: Equal polynomial
    poly_f = [[0, 1], [1, 1]]
    poly_g = [[0, 2], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert not f.equal_poly(g)


def test_SparsePoly_44():
    # Test: Not equal polynomial
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    g = SparsePoly(poly)
    assert not f.not_equal_poly(g)


def test_SparsePoly_45():
    # Test: Not equal polynomial
    poly_f = [[0, 1], [1, 1]]
    poly_g = [[0, 2], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.not_equal_poly(g)


def test_SparsePoly_46():
    # Test: Copy polynomial
    poly_f = [[0, 1], [1, 1]]
    f = SparsePoly(poly_f)
    g = f.copy_poly()
    assert f.equal_poly(g)


def test_SparsePoly_47():
    # Test: Copy polynomial
    poly_f = [[0, 1], [1, 1]]
    f = SparsePoly(poly_f)
    g = f.copy_poly()
    f.coeffpairs[0][0] += 1
    assert f.not_equal_poly(g)


def test_SparsePoly_48():
    # Test: add x+1 to itself
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    g = SparsePoly(poly)
    assert f.add_poly(g).print_poly() == '2x+2'


def test_SparsePoly_49():
    # Test: add x+1 to -x-1
    poly_f = [[0, 1], [1, 1]]
    poly_g = [[0, -1], [1, -1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.add_poly(g).print_poly() == '0'


def test_SparsePoly_50():
    # Test: add x^100+1 to x^101-1 itself
    poly_f = [[0, 1], [100, 1]]
    poly_g = [[0, -1], [101, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.add_poly(g).print_poly() == 'x^101+x^100'


def test_SparsePoly_51():
    # Test: add two bigger polys
    poly_f = [[0, 1], [2, 1], [3, 2], [4, -1]]
    poly_g = [[0, -1], [3, 5], [4, 4], [5, 2]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.add_poly(g).print_poly() == '2x^5+3x^4+7x^3+x^2'



def test_SparsePoly_52():
    # Test: add zero polynomial
    poly_f = [[0, 1], [1, 1]]
    poly_g = [[0, 0]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.add_poly(g).print_poly() == 'x+1'


def test_SparsePoly_53():
    # Test: Negate x+1
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.negate_poly().print_poly() == '-x-1'


def test_SparsePoly_54():
    # Test: Negate -1
    poly = [[0, -1]]
    f = SparsePoly(poly)
    assert f.negate_poly().print_poly() == '1'


def test_SparsePoly_55():
    # Test: Negate -1
    poly = [[0, 0]]
    f = SparsePoly(poly)
    assert f.negate_poly().print_poly() == '0'


def test_SparsePoly_56():
    # Test: Subtract x+1 from x^2+x+1
    poly_f = [[0, 1], [1, 1], [2, 1]]
    poly_g = [[0, 1], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.subtract_poly(g).print_poly() == 'x^2'


def test_SparsePoly_57():
    # Test: Subtract x^2+x+1 from x+1
    poly_f = [[0, 1], [1, 1]]
    poly_g = [[0, 1], [1, 1], [2, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.subtract_poly(g).print_poly() == '-x^2'


def test_SparsePoly_58():
    # Test: Subtract zero poly from x+1
    poly_f = [[0, 1], [1, 1]]
    poly_g = [[0, 0]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.subtract_poly(g).print_poly() == 'x+1'


def test_SparsePoly_59():
    # Test: Subtract from zero equals negation
    poly_f = [[0, 1], [1, 1]]
    poly_g = [[0, 0]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert g.subtract_poly(f).print_poly() == f.negate_poly().print_poly()


def test_SparsePoly_60():
    # Test: Multiply x+1 and x^2+x+1
    poly_f = [[0, 1], [1, 1], [2, 1]]
    poly_g = [[0, 1], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.multiply_poly(g).print_poly() == 'x^3+2x^2+2x+1'


def test_SparsePoly_61():
    # Test: Multiply x^2x+1 and 1
    poly_f = [[0, 1], [1, 1], [2, 1]]
    poly_g = [[0, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.multiply_poly(g).print_poly() == f.print_poly()


def test_SparsePoly_62():
    # Test: Multiply by -1 equalling negation
    poly_f = [[0, 1], [1, 1], [2, 1]]
    poly_g = [[0, -1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.multiply_poly(g).print_poly() == f.negate_poly().print_poly()


def test_SparsePoly_63():
    # Test: Multiply by 0 equalling zero poly
    poly_f = [[0, 1], [1, 1], [2, 1]]
    poly_g = [[0, 0]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.multiply_poly(g).print_poly() == '0'


def test_SparsePoly_64():
    # Test: Divide x^2 - 1 by 0
    poly_f = [[0, -1], [2, 1]]
    poly_g = [[0, 0]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    q, r = f.divide_poly(g)
    assert q.printpoly() == '0'
    assert r.printpoly() == 'x^2-1'


def test_SparsePoly_65():
    # Test: Divide x^2 - 1 by itself
    poly_f = [[0, -1], [2, 1]]
    f = SparsePoly(poly_f)
    g = f.copy_poly()
    q, r = f.divide_poly(g)
    assert q.printpoly() == '1'
    assert r.printpoly() == '0'


def test_SparsePoly_66():
    # Test: Divide x^2 - 1 by x-1
    poly_f = [[0, -1], [2, 1]]
    poly_g = [[0, -1], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    q, r = f.divide_poly(g)
    assert q.printpoly() == 'x+1'
    assert r.printpoly() == '0'


def test_SparsePoly_67():
    # Test: Divide x^2 - 1 by x+12
    poly_f = [[0, -1], [2, 1]]
    poly_g = [[0, 12], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    q, r = f.divide_poly(g)
    assert q.printpoly() == 'x-12.0'
    assert r.printpoly() == '143.0'


def test_SparsePoly_68():
    # Test: Divide 3x^5 + 2x^4 + x^2 - 1 by x^2+12
    poly_f = [[0, -1], [2, 1], [4, 2], [5, 3]]
    poly_g = [[0, 12], [2, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    q, r = f.divide_poly(g)
    assert q.printpoly() == '3.0x^3+2.0x^2-36.0x-23.0'
    assert r.printpoly() == '432.0x+275.0'


def test_SparsePoly_69():
    # Test: Differentiate 3x^2+x+1 
    poly = [[0, 1], [1, 1], [2, 3]]
    f = SparsePoly(poly)
    assert f.differentiate_poly().print_poly() == '6x+1'


def test_SparsePoly_70():
    # Test: Differentiate 1 
    poly = [[0, 1]]
    f = SparsePoly(poly)
    assert f.differentiate_poly().print_poly() == '0'


def test_SparsePoly_71():
    # Test: Differentiate 0
    poly = [[0, 0]]
    f = SparsePoly(poly)
    assert f.differentiate_poly().print_poly() == '0'


def test_SparsePoly_72():
    # Test: Integrate x+1 
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.integrate_poly().print_poly() == '0.5x^2+x'


def test_SparsePoly_73():
    # Test: Integrate x+1 with constant
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.integrate_poly(10).print_poly() == '0.5x^2+x+10'


def test_SparsePoly_74():
    # Test: Integrate 0 
    poly = [[0, 0]]
    f = SparsePoly(poly)
    assert f.integrate_poly().print_poly() == '0'


def test_SparsePoly_75():
    # Test: Integrate 0 with constant
    poly = [[0, 0]]
    f = SparsePoly(poly)
    assert f.integrate_poly(10).print_poly() == '10'

def test_SparsePoly_76():
    # Test: Definite integral x+1 
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.definite_integral(10, 15) == 67.5


def test_SparsePoly_77():
    # Test: Definite integral x^2+x+1 
    poly = [[0, 1], [1, 1], [2, 1]]
    f = SparsePoly(poly)
    assert "%.1f" % f.definite_integral(0, 50) == '42966.7'


def test_SparsePoly_78():
    # Test: Definite integral 0 
    poly = [[0, 0]]
    f = SparsePoly(poly)
    assert f.definite_integral(0, 50) == 0


def test_SparsePoly_79():
    # Test: Definite integral with floats 
    poly = [[0, 1]]
    f = SparsePoly(poly)
    assert "%.5f" % f.definite_integral(5.00001, 5.12346) == '0.12345'


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
    # Test: cannot solve zero polynomial
    poly = [[0, 0]]
    f = SparsePoly(poly)
    try:
        f.numeric_solve_poly()
        assert False
    except Exception as e:
        assert e.args[0] == 'Cannot solve constant polynomials.'

def test_Solving_Poly_5():
    # Test: solve x+1
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.numeric_solve_poly() == [-1.0]


def test_Solving_Poly_6():
    # Test: solve 2x+1
    poly = [[0, 1], [1, 2]]
    f = SparsePoly(poly)
    assert f.numeric_solve_poly() == [-0.5]


def test_Solving_Poly_7():
    # Test: solve (x-1)(x-2)
    poly_f = [[0, -1], [1, 1]]
    poly_g = [[0, -2], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.multiply_poly(g).numeric_solve_poly() == [1.0, 2.0]


def test_Solving_Poly_8():
    # Test: solve x^2-2
    poly = [[0, -2], [2, 1]]
    f = SparsePoly(poly)
    assert "%.3f" % f.numeric_solve_poly()[0] == '-1.414'
    assert "%.3f" % f.numeric_solve_poly()[1] == '1.414'


def test_Solving_Poly_9():
    # Test: solve (x-1)(x-1)
    poly = [[0, -1], [1, 1]]
    f = SparsePoly(poly)
    assert f.multiply_poly(f).numeric_solve_poly() == [1.0]


def test_Solving_Poly_10():
    # Test: solve x^2+1
    poly = [[0, 1], [2, 1]]
    f = SparsePoly(poly)
    assert f.numeric_solve_poly() == []


def test_Solving_Poly_11():
    # Test: solve x^3-1
    poly = [[0, -1], [3, 1]]
    f = SparsePoly(poly)
    assert f.numeric_solve_poly() == [1.0]


def test_Solving_Poly_12():
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
#     print f.multiply_poly(g).print_poly()
#     print f.multiply_poly(g).numeric_solve_poly()
#     assert f.multiply_poly(g).numeric_solve_poly() == [4.0]








def test_Solving_Poly_1s():
    # Test: cannot solve quartic
    poly = [[0, 1], [1, 1], [4, 1]]
    f = SparsePoly(poly)
    try:
        f.symbolic_solve_poly()
        assert False
    except Exception as e:
        assert e.args[0] == 'Cannot solve polynomials of degree 4.'


def test_Solving_Poly_2s():
    # Test: cannot solve degree 1000
    poly = [[0, 1], [1, 1], [1000, 1]]
    f = SparsePoly(poly)
    try:
        f.symbolic_solve_poly()
        assert False
    except Exception as e:
        assert e.args[0] == 'Cannot solve polynomials of degree 1000.'


def test_Solving_Poly_3s():
    # Test: cannot solve constant
    poly = [[0, 1]]
    f = SparsePoly(poly)
    try:
        f.symbolic_solve_poly()
        assert False
    except Exception as e:
        assert e.args[0] == 'Cannot solve constant polynomials.'


def test_Solving_Poly_4s():
    # Test: cannot solve zero polynomial
    poly = [[0, 0]]
    f = SparsePoly(poly)
    try:
        f.symbolic_solve_poly()
        assert False
    except Exception as e:
        assert e.args[0] == 'Cannot solve constant polynomials.'

def test_Solving_Poly_5s():
    # Test: solve x+1
    poly = [[0, 1], [1, 1]]
    f = SparsePoly(poly)
    assert f.symbolic_solve_poly() == ['-1']


def test_Solving_Poly_6s():
    # Test: solve 2x+1
    poly = [[0, 1], [1, 2]]
    f = SparsePoly(poly)
    assert f.symbolic_solve_poly() == ['-1/2']


def test_Solving_Poly_7s():
    # Test: solve (x-1)(x-2)
    poly_f = [[0, -1], [1, 1]]
    poly_g = [[0, -2], [1, 1]]
    f = SparsePoly(poly_f)
    g = SparsePoly(poly_g)
    assert f.multiply_poly(g).symbolic_solve_poly() == ['[3±1]/2']


def test_Solving_Poly_8s():
    # Test: solve x^2-2
    poly = [[0, -2], [2, 1]]
    f = SparsePoly(poly)
    assert f.symbolic_solve_poly() == ['[0±√[8]]/2']


def test_Solving_Poly_9s():
    # Test: solve (x-1)(x-1)
    poly = [[0, -1], [1, 1]]
    f = SparsePoly(poly)
    assert f.multiply_poly(f).symbolic_solve_poly() == ['1']


def test_Solving_Poly_10s():
    # Test: solve x^2+1
    poly = [[0, 1], [2, 1]]
    f = SparsePoly(poly)
    assert f.symbolic_solve_poly() == ['[0±√[-4]]/2']


# TODO: We need to do better simplification so we can improve above
# tests and these ones below


# def test_solve_quad_symbolic_1():
#     # Test: solve quad symbolic
#     poly = [5, 7, 1]
#     assert solve_quad_symbolic(poly) == "[-7±√[29]]/2"


# def test_solve_quad_symbolic_2():
#     # Test: solve quad symbolic
#     poly = [15, -8, 1]
#     assert solve_quad_symbolic(poly) == "[8±√[4]]/2"


# def test_solve_quad_symbolic_3():
#     # Test: solve quad symbolic - discriminant zero
#     poly = [2, 4, 2]
#     assert solve_quad_symbolic(poly) == "1"


# def test_solve_quad_symbolic_4():
#     # Test: solve quad symbolic - negative discriminant
#     poly = [2, 4, 4]
#     assert solve_quad_symbolic(poly) == "[-4±√[-16]]/8"

