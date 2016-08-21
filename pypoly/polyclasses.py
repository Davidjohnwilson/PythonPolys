# coding: utf-8
from __future__ import division

# Polynomial classes
from math import sqrt


# General Polynomial Class


class Polynomial(object):
    'Polynomials of any type'
    # Empty class currently just for inheritance.

# dense polynomial
# We store an array with all the coefficients for every degree


class DensePoly(Polynomial):
    'Polynomials stored in a dense manner'
    coeffs = []

    def __init__(self, coeffs):
        if not type(coeffs) is list:
            raise Exception('Not a valid polynomial')
        if len(coeffs) == 0:
            raise Exception('Not a valid polynomial')
        for i in coeffs:
            if not type(i) in (int, float):
                raise Exception('Not a valid polynomial')

        tmp_coeffs = coeffs
        # Remove any trailing 0's
        while tmp_coeffs and len(tmp_coeffs) > 1 and (tmp_coeffs[-1] == 0):
            tmp_coeffs.pop()
        self.coeffs = tmp_coeffs

    def degree(self):
        # degree is just the length of the vector of coefficients minus 1
        # (as we don't store trailing 0 coefficients)
        n = len(self.coeffs)
        if (n == 0) or (n == 1 and self.coeffs[0] == 0):
            # The degree of the zero polynomial is undefined so is often
            # defined as either -Inf or -1. We choose -1 as it is more
            # straightforward to check for.
            return -1
        else:
            return n - 1

    def print_poly(self, variable='x'):
        # Printing polynomial with placeholder 'x'
        polyarr = []
        dummy_variable = variable
        n = len(self.coeffs)
        # Note we know n>0 because of class checks
        for i in range(1, n - 1):
            # we work backwards
            if self.coeffs[n - i] not in [0, 1, -1]:
                polyarr.append(str(self.coeffs[n - i]) +
                               dummy_variable + '^' + str(n - i))
            elif self.coeffs[n - i] == 1:
                polyarr.append(dummy_variable + '^' + str(n - i))
            elif self.coeffs[n - i] == -1:
                polyarr.append('-' + dummy_variable + '^' + str(n - i))
        if n > 1 and self.coeffs[1] != 0:
            if self.coeffs[1] == 1:
                polyarr.append(dummy_variable)
            elif self.coeffs[1] == -1:
                polyarr.append('-' + dummy_variable)
            else:
                polyarr.append(str(self.coeffs[1]) + dummy_variable)
        if n == 1 or self.coeffs[0] != 0:
            polyarr.append(str(self.coeffs[0]))
        return '+'.join(polyarr).replace('+-', '-')

    def eval_poly(self, x):
        # Let's use Horner!
        n = len(self.coeffs)
        val = self.coeffs[n - 1]
        for i in range(1, n):
            val = self.coeffs[n - (i + 1)] + (val * x)
        return val

    def to_sparse_poly(self):
        polyarr = []
        n = len(self.coeffs)
        for i in range(n):
            if self.coeffs[i] != 0:
                polyarr.append([i, self.coeffs[i]])
        return SparsePoly(polyarr)


# Sparse Poly
# We store polynomials in a sparse format - an array of
# arrays of the form [exponent, coefficient]

class SparsePoly(Polynomial):
    'Polynomials stored in a sparse manner ([exp, coeff])'
    coeffpairs = []

    def __init__(self, coeffpairs):
        # Check for validity when initializing polynomial
        if not type(coeffpairs) is list:
            raise Exception('Not a valid polynomial')
        if len(coeffpairs) == 0:
            raise Exception('Not a valid polynomial')
        for l in coeffpairs:
            if not type(l) is list:
                raise Exception('Not a valid polynomial')
            for i in l:
                if not type(i) in (int, float):
                    raise Exception('Not a valid polynomial')
            if l[0] < 0:
                raise Exception('Not a valid polynomial')

        # We simplify the coefficients. This combines any coefficients
        # for the same degree.
        coeff_dict = {}
        for c in coeffpairs:
            if c[0] in coeff_dict:
                coeff_dict[c[0]] += c[1]
            else:
                coeff_dict[c[0]] = c[1]
        new_coeffs = []
        for k in coeff_dict:
            if coeff_dict[k] != 0:
                new_coeffs.append([k, coeff_dict[k]])
        if len(new_coeffs) == 0:
            new_coeffs = [[0, 0]]
        # We sort the coeffs - this is partly to print nicely and
        # it can also save some time in evaluating due to storing
        # the previously computed power.
        self.coeffpairs = sorted(new_coeffs, key=lambda x: x[0])

    def degree(self):
        # to check degree we look for largest degree
        non_zero_coeffs = [c[0] for c in self.coeffpairs if c[1] != 0]
        if len(non_zero_coeffs) > 0:
            return max(non_zero_coeffs)
        else:
            return -1

    def print_poly(self, variable='x'):
        # print polynomial in reverse order
        polyarr = []
        for c in reversed(self.coeffpairs):
            if c[0] == 0:
                # We treat the constant term separately
                if c[1] == 1.0:
                    polyarr.append('1')
                elif c[1] == -1.0:
                    polyarr.append('-1')
                else:
                    polyarr.append(str(c[1]))
            elif c[0] == 1:
                # We treat the single exponent term separately
                if c[1] == 1 or c[1] == 1.0:
                    polyarr.append(variable)
                elif c[1] == -1 or c[1] == -1.0:
                    polyarr.append('-' + variable)
                else:
                    polyarr.append(str(c[1]) + variable)
            elif c[1] == 1 or c[1] == 1.0:
                polyarr.append(variable + '^' + str(c[0]))
            elif c[1] == -1 or c[1] == -1.0:
                polyarr.append('-' + variable + '^' + str(c[0]))
            else:
                polyarr.append(str(c[1]) + variable + '^' + str(c[0]))
        return '+'.join(polyarr).replace('+-', '-')

    def eval_poly(self, x):
        # naive evaluation
        # We store partial power values to try and save on computation
        # Much quicker when powers in ascending order which should be
        # expected from initializing.
        val = 0
        current_pow = 0
        current_pow_val = 1
        for c in self.coeffpairs:
            current_pow_val = current_pow_val * pow(x, c[0] - current_pow)
            current_pow = c[0]
            val += c[1] * current_pow_val
            # We have eliminated the following code
            # if c[0] >= current_pow: *do as above*
            # else:
            # current_pow_val = pow(x, c[0])
            # current_pow = c[0]

        return val

    def to_dense_poly(self):
        deg = self.degree()
        polyarr = [0 for _ in range(deg + 1)]
        for c in self.coeffpairs:
            polyarr[c[0]] = c[1]
        return DensePoly(polyarr)

    def simplify_poly(self):
        # This function simplifies a polynomial down
        # in particular if any term has a zero coefficient
        coeffs = self.coeffpairs
        coeff_dict = {}
        for c in coeffs:
            if c[0] in coeff_dict:
                coeff_dict[c[0]] += c[1]
            else:
                coeff_dict[c[0]] = c[1]
        new_coeffs = []
        for k in coeff_dict:
            if coeff_dict[k] != 0:
                new_coeffs.append([k, coeff_dict[k]])
        if len(new_coeffs) == 0:
            new_coeffs = [[0, 0]]
        return SparsePoly(sorted(new_coeffs, key=lambda x: x[0]))

    def simplify_poly_inplace(self):
        # This function works like simplify_poly but does so
        # in place.
        h = self.simplify_poly()
        self.coeffpairs = h.coeffpairs

    def equal_poly(self, g):
        f_s = self.simplify_poly()
        g_s = g.simplify_poly()
        return f_s.coeffpairs == g_s.coeffpairs

    def not_equal_poly(self, g):
        f_s = self.simplify_poly()
        g_s = g.simplify_poly()
        return f_s.coeffpairs != g_s.coeffpairs

    def copy_poly(self):
        return SparsePoly(self.coeffpairs)

    def add_poly(self, g):
        # We allow for DensePoly by converting
        # Addition is simply appending two arrays and simplify
        poly_two = g
        # Having to use this hack as not sure why it doesn't work
        # for python 2.7
        if poly_two.__class__.__name__ == 'DensePoly':
            poly_two = poly_two.to_sparse_poly()
        new_coeffpairs = self.coeffpairs + poly_two.coeffpairs
        return SparsePoly(new_coeffpairs).simplify_poly()

    def negate_poly(self):
        # Negating a polynomial is just negating coefficients
        # Note we have to create a new array to avoid changing
        # coeffpairs inplace.
        coeffs = []
        for c in self.coeffpairs:
            coeffs.append([c[0], -c[1]])
        return SparsePoly(coeffs)

    def subtract_poly(self, g):
        # To subtract we negate and add
        return self.add_poly(g.negate_poly()).simplify_poly()

    def multiply_poly(self, g):
        # Multiplying is done my combining lists and simplifying
        coeffs = self.coeffpairs
        g_coeffs = g.coeffpairs
        mult_coeffs = [[f_c[0] + g_c[0], f_c[1] * g_c[1]]
                       for f_c in coeffs for g_c in g_coeffs]
        return SparsePoly(mult_coeffs).simplify_poly()

    def divide_poly(self, g):
        # We compute f/g and return an array [q,r] such that
        #        f = q*g + r

        # Initialize with q = 0, r = f
        q = SparsePoly([[0, 0]])
        r = self.copy_poly()

        # First check if g == 0
        zero_poly = SparsePoly([[0, 0]])
        if g.equal_poly(zero_poly):
            return [q, r]

        g_degree = g.degree()

        while r.not_equal_poly(zero_poly) and r.degree() >= g_degree:
            t_term = [r.coeffpairs[-1][0] - g.coeffpairs[-1][0],
                      1.0 * r.coeffpairs[-1][1] / g.coeffpairs[-1][1]]
            t = SparsePoly([t_term])
            q = q.add_poly(t)
            s = t.multiply_poly(g)
            r = r.subtract_poly(s)

        return [q, r]

    def differentiate_poly(self):
        # To differentiate we just alter each coefficient
        coeffs = self.coeffpairs
        diff_coeffs = []
        for c in coeffs:
            if c[0] != 0:
                diff_coeffs.append([c[0] - 1, c[0] * c[1]])
        if len(diff_coeffs) == 0:
            diff_coeffs = [[0, 0]]
        return SparsePoly(diff_coeffs)

    def integrate_poly(self, C=0):
        # We allow for an arbitrary choice of integration constant (default 0)
        # Note we also end up with non-integer coefficients
        coeffs = self.coeffpairs
        int_coeffs = []
        if C != 0:
            int_coeffs.append([0, C])
        for c in coeffs:
            int_coeffs.append([c[0] + 1, 1.0 * c[1] / (c[0] + 1)])
        return SparsePoly(int_coeffs)

    def definite_integral(self, a, b):
        # To compute the definite integral we just combine integration
        # and evaluation.
        return (self.integrate_poly().eval_poly(b) -
                self.integrate_poly().eval_poly(a))

    def numeric_solve_poly(self):
        # Solves polynomial and returns a list of real solutions
        if self.degree() < 1:
            # Note that <1 includes zero polynomial
            raise Exception('Cannot solve constant polynomials.')
        elif self.degree() > 3:
            raise Exception('Cannot solve polynomials of degree %i.'
                            % self.degree())

        # linear polynomials
        if self.degree() == 1:
            a = 0
            b = 0
            for c_p in self.coeffpairs:
                if c_p[0] == 1:
                    a = c_p[1]
                elif c_p[0] == 0:
                    b = c_p[1]
            return [1.0 * (-b) / a]

        # quadratic polynomials
        if self.degree() == 2:
            a = 0
            b = 0
            c = 0
            for c_p in self.coeffpairs:
                if c_p[0] == 2:
                    a = c_p[1]
                elif c_p[0] == 1:
                    b = c_p[1]
                elif c_p[0] == 0:
                    c = c_p[1]

            # Note that as degree==2 we know a != 0

            discrim = b * b - 4 * a * c

            if discrim == 0:
                return [1.0 * -b / (2 * a)]
            elif discrim > 0:
                return sorted([(1.0 * -b + sqrt(discrim)) / (2 * a),
                               (1.0 * -b - sqrt(discrim)) / (2 * a)])
            else:
                return []

        # cubic polynomials
        if self.degree() == 3:
            a = 0
            b = 0
            c = 0
            d = 0
            for c_p in self.coeffpairs:
                if c_p[0] == 3:
                    a = c_p[1]
                elif c_p[0] == 2:
                    b = c_p[1]
                elif c_p[0] == 1:
                    c = c_p[1]
                elif c_p[0] == 0:
                    d = c_p[1]
            p = 1.0 * -b / (3 * a)
            q = 1.0 * p * p * p + ((b * c - 3 * a * d) / (6 * a * a))
            r = 1.0 * c / (3 * a)
            x = pow(q + sqrt(q ** 2 + pow((r - p ** 2), 1)), 1 / 3.0) + \
                pow(q - sqrt(q ** 2 + pow((r - p ** 2), 1)), 1 / 3.0) + p
            return [x]

    def symbolic_solve_poly(self):
        # Solves polynomial symbolically and returns a list of strings
        # representing real solutions
        if self.degree() < 1:
            # Note that <1 includes zero polynomial
            raise Exception('Cannot solve constant polynomials.')
        elif self.degree() > 3:
            raise Exception('Cannot solve polynomials of degree %i.'
                            % self.degree())

        # linear polynomials
        if self.degree() == 1:
            a = 0
            b = 0
            for c_p in self.coeffpairs:
                if c_p[0] == 1:
                    a = c_p[1]
                elif c_p[0] == 0:
                    b = c_p[1]
            if b >= a and b % a == 0:
                return [str(int(-b / a))]
            else:
                return ['%i/%i' % (-b, a)]

        # quadratic polynomials
        if self.degree() == 2:
            a = 0
            b = 0
            c = 0
            for c_p in self.coeffpairs:
                if c_p[0] == 2:
                    a = c_p[1]
                elif c_p[0] == 1:
                    b = c_p[1]
                elif c_p[0] == 0:
                    c = c_p[1]

            # Note that as degree==2 we know a != 0
            discrim = b * b - 4 * a * c

            if discrim == 0:
                if b % (2 * a) == 0:
                    return ['%i' % int(-b / (2 * a))]
                else:
                    return ['%i/%i' % (-b, (2 * a))]
            elif discrim > 0:

                # Square root exact
                if sqrt(discrim) == int(sqrt(discrim)):
                    return ['[%i±%i]/%i' % (-b, sqrt(discrim), 2 * a)]

                # Not exact
                return ['[%i±√[%i]]/%i' % (-b, discrim, 2 * a)]
            else:
                return ['[%i±√[%i]]/%i' % (-b, discrim, 2 * a)]
