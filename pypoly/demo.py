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

print(full_line)

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

press_enter()

print(full_line)

print("We will now focus primarily on SparsePoly objects as they have ")
print("greater functionality.")

press_enter()

print("One of the most fundamental properties of a polynomial is its  ")
print("degree, which can be found using the function of the same name.")
print("   > f = SparsePoly([[0, 1], [3, 5]])                          ")
f = SparsePoly([[0, 1], [3, 5]])
print("   > f.print_poly()                                            ")
print("              " + f.print_poly())
print("   > f.degree()                                                ")
print("              " + str(f.degree()))
print("   > f = SparsePoly([[0, 1], [100, 5], [1000, 10]])            ")
f = SparsePoly([[0, 1], [100, 5], [1000, 10]]) 
print("   > f.print_poly()                                            ")
print("              " + f.print_poly())
print("   > f.degree()                                                ")
print("              " + str(f.degree()))

press_enter()

print("We can also evaluate a polynomial at any value. This is done   ")
print("with the eval_poly(x) function. Note that this method uses the ")
print("fact that the terms are in increasing order of power to reduce ")
print("computation, storing and using the previously computed power.  ")
print("   > f = SparsePoly([[0, 1], [3, -5], [5, 1]])                 ")
f = SparsePoly([[0, 1], [3, -5], [5, 1]])
print("   > f.print_poly()                                            ")
print("              " + f.print_poly())
print("   > f.eval_poly(1)                                            ")
print("              " + str(f.eval_poly(1)))
print("   > f.eval_poly(10)                                          ")
print("              " + str(f.eval_poly(100)))

press_enter()

print("We can manipulate polynomials with the basic operations: negation,")
print("addition, subtraction, and multiplication.                        ")
print("These actions are done by calling a function on the first         ")
print("polynomial, passing the second (if required) polynomial as a      ")
print("parameter, and a third polynomial (the result) is returned.       ")
print("   > f = SparsePoly([[0, 1], [3, -5], [5, 1]])                    ")
f = SparsePoly([[0, 1], [3, -5], [5, 1]])
print("   > g = SparsePoly([[0, -1], [2, 4], [3, 1]])                    ")
g = SparsePoly([[0, -1], [2, 4], [3, 1]])
print("   > f.print_poly()                                               ")
print("              " + f.print_poly())
print("   > g.print_poly()                                               ")
print("              " + g.print_poly())
print("   > f.negate_poly().print_poly()                                 ")
print("              " + f.negate_poly().print_poly())
print("   > f.add_poly(g).print_poly()                                   ")
print("              " + f.add_poly(g).print_poly())
print("   > f.subtract_poly(g).print_poly()                              ")
print("              " + f.subtract_poly(g).print_poly())
print("   > f.multiply_poly(g).print_poly()                              ")
print("              " + f.multiply_poly(g).print_poly())

# TODO This can only be used once division is merged.

# press_enter()

# print("We can also do polynomial 'long division'. That is, given two     ")
# print("polynomials, f and g, we can return two polynomials, q and r, such")
# print("that the following equation holds:                                ")
# print("                f = q * g + r                                     ")
# print("We can produce the quotient and remainder using divide_poly, which")
# print("returns an array of the two polynomials.                          ")
# print("   > f = SparsePoly([[0, -1], [3, 1]])                            ")
# f = SparsePoly([[0, -1], [3, 1]])
# print("   > g = SparsePoly([[0, -1], [1, 1]])                            ")
# g = SparsePoly([[0, -1], [1, 1]])
# print("   > f.print_poly()                                               ")
# print("              " + f.print_poly())
# print("   > g.print_poly()                                               ")
# print("              " + g.print_poly())
# print("   > q, r = f.divide_poly(g)                                      ")
# q, r = f.divide_poly(g)
# print("   > q.print_poly()                                               ")
# print("              " + q.print_poly())
# print("   > r.print_poly()                                               ")
# print("              " + r.print_poly())
# print("We can check by multiplying and adding the polynomials together.  ")
# print("   > g.multiply_poly(q).add_poly(r).print_poly()                  ")
# print("              " + g.multiply_poly(q).add_poly(r).print_poly())

press_enter()

print("We can do basic calculus functions such as differentiation and   ")
print("integration. As we are just dealing with polynomials these are   ")
print("always possible.                                                 ")
print("   > f = SparsePoly([[0, 1], [3, -5], [5, 1]])                   ")
f = SparsePoly([[0, 1], [3, -5], [5, 1]])
print("   > f.print_poly()                                              ")
print("              " + f.print_poly())
print("   > f.differentiate_poly().print_poly()                         ")
print("              " + f.differentiate_poly().print_poly())
print("   > f.differentiate_poly().differentiate_poly().print_poly()    ")
print("              " + f.differentiate_poly().differentiate_poly().print_poly())
print("When we integrate we have the option to include a constant of    ")
print("integration, or to default it to zero.                           ")
print("   > f.integrate_poly().print_poly()                             ")
print("              " + f.integrate_poly().print_poly())
print("   > f.integrate_poly(10).print_poly()                           ")
print("              " + f.integrate_poly(10).print_poly())
print("Finally, we can do definite integrals between two constants.     ")
print("   > f.definite_integral(10, 15).print_poly()                    ")
print("              " + str(f.definite_integral(10, 15)))


press_enter()

print("Numeric Solve")

press_enter()

print("Symbolic solve")

print(full_line)
