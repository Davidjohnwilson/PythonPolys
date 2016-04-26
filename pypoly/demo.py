# coding: utf-8

import sys
import os
sys.path.append(os.path.abspath("./pypoly"))
from polyclasses import *

# ==================================
# Demo file for pypoly
# ==================================
blank_line = "                                                      "


print("# ====================================================== #")
print("#                Demo File for the                       #")
print("#                        pypoly package                  #")
print("# ====================================================== #")

print("This file is intended to demo the pypoly package. For ")
print("further information please visit the repo:            ")
print("      github.com/DavidJohnWilson/PythonPolys          ")

print(blank_line)
print(blank_line)

print("We will demo the DensePoly and SparsePoly classes, including")
print("Some of their methods.")

print(blank_line)

print("The DensePoly is a dense representation of polynomials. This")
print("means you simply list the coefficients of ascending powers  ")
print("of the polynomial.                                          ")
print("For example, to define 3x^2+2+1 we would use the command:   ")
print("        f = DensePoly([1, 2, 3])                            ")

f = DensePoly([1, 2, 3])

print("We can check this is the correct polynomial by using the       ")
print("print_poly command, to give a representation of the polynomial.")
print(blank_line)
print("   > f.print_poly()                                            ")
print("              " + f.print_poly())
