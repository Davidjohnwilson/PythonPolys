# coding: utf-8

import sys
import os
sys.path.append(os.path.abspath("./pypoly"))
from polyclasses import *

# ==================================
# Demo file for pypoly
# ==================================
blank_line = "                                                      "
full_line = "================================================================"

def press_enter():
    print(blank_line)
    print(blank_line)
    try:
        raw_input("Press enter to continue")
    except SyntaxError:
        pass
    except NameError:
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass
    print(blank_line)
    print(blank_line)



print("# ====================================================== #")
print("#                Demo File for the                       #")
print("#                        pypoly package                  #")
print("# ====================================================== #")

print("This file is intended to demo the pypoly package. For ")
print("further information please visit the repo:            ")
print("      github.com/DavidJohnWilson/PythonPolys          ")

print(blank_line)

print("We will demo the DensePoly and SparsePoly classes, including")
print("some of their methods.")

press_enter()

print("The DensePoly is a dense representation of polynomials. This")
print("means you simply list the coefficients of ascending powers  ")
print("of the polynomial.                                          ")
print("For example, to define 3x^2-7x+1 we would use the command:  ")
print("   > f = DensePoly([1, -7, 3])                              ")

f = DensePoly([1, -7, 3])

print("We can access the list of coefficients easily with coeffs. Note")
print("that trailing zeros are removed (as they do not contribute to  ")
print("the polynomial.")
print("   > f = DensePoly([1, -7, 3, 0, 0])                           ")
f = DensePoly([1, -7, 3, 0, 0])
print("   > f.coeffs                                                  ")
print("              " + str(f.coeffs))

press_enter()

print("We can check this is the correct polynomial by using the       ")
print("print_poly command, to give a representation of the polynomial.")
print("   > f.print_poly()                                            ")
print("              " + f.print_poly())

press_enter()

print("The SparsePoly is a sparse representation of polynomials.   ")
print("This means you list the exponent and coefficient of each    ")
print("term of the polynomial.                                     ")
print("For example, to define 3x^2-7x+1 we would use the command:  ")
print("   > g = SparsePoly([[0, 1], [1, -7], [2, 3]])              ")

g = SparsePoly([[0, 1], [1, -7], [2, 3]])


print("We can access the list of terms easily with coeffpairs. Note   ")
print("that terms are simplified and any with a zero coefficient are  ")
print("removed from the polynomial.")
print("   > g = SparsePoly([[0, 1], [1, -7], [2, 3], [5, 0]])         ")
g = SparsePoly([[0, 1], [1, -7], [2, 3], [5, 0]])
print("   > g.coeffpairs                                              ")
print("              " + str(g.coeffpairs))

press_enter()

print("We can check this is the correct polynomial by using the       ")
print("print_poly command, to give a representation of the polynomial.")
print("   > g.print_poly()                                            ")
print("              " + g.print_poly())

press_enter()

print("We can convert between the polynomial representations by using ")
print("the to_sparse_poly and to_dense_poly functions.                ")
print("   > f = DensePoly([1, -7, 3])                                 ")
f = DensePoly([1, -7, 3])
print("   > g = f.to_sparse_poly()                                    ")
g = f.to_sparse_poly()
print("   > g.coeffpairs                                              ")
print("              " + str(g.coeffpairs))
print("   > [isinstance(f, DensePoly), isinstance(g, SparsePoly)]     ")
print("              " + str([isinstance(f, DensePoly), isinstance(g, SparsePoly)]))
print("   > [f.print_poly(), g.print_poly()]                          ")
print("              " + str([f.print_poly(), g.print_poly()]))

print(full_line)
