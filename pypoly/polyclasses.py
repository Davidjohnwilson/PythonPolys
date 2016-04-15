# coding: utf-8
from __future__ import division

# Polynomial classes
from math import pow


# General Polynomial Class


class Polynomial:
    'Polynomials of any type'

    def __init__(self):
        pass


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
            if not type(i) is int:
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

    def printpoly(self, variable='x'):
        # Printing polynomial with placeholder 'x'
        polyarr = []
        dummy_variable = variable
        n = len(self.coeffs)
        if n == 0:
            return ''
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

    def evalpoly(self, x):
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

# print("f = DensePoly([3,2,5]):")
# f = DensePoly([3,2,5])
# print(f.degree())
# print(f.printpoly())
# print(f.evalpoly(2))

# Sparse Poly


class SparsePoly(Polynomial):
    'Polynomials stored in a sparse manner'
    coeffpairs = []

    def __init__(self, coeffpairs):
        if not type(coeffpairs) is list:
            raise Exception('Not a valid polynomial')
        if len(coeffpairs) == 0:
            raise Exception('Not a valid polynomial')
        for l in coeffpairs:
            if not type(l) is list:
                raise Exception('Not a valid polynomial')
            for i in l:
                if not type(i) is int:
                    raise Exception('Not a valid polynomial')
            if l[0] < 0:
                raise Exception('Not a valid polynomial')
        self.coeffpairs = sorted(coeffpairs, key=lambda x: x[0])

    def degree(self):
        # to check degree we look for largest degree
        non_zero_coeffs = [c[0] for c in self.coeffpairs if c[1] != 0]
        if len(non_zero_coeffs) > 0:
            return max(non_zero_coeffs)
        else:
            return -1

    def printpoly(self, variable='x'):
        # print polynomial
        polyarr = []
        for c in reversed(self.coeffpairs):

            if c[0] == 0:
                polyarr.append(str(c[1]))
            elif c[0] == 1:
                if c[1] == 1:
                    polyarr.append(variable)
                elif c[1] == -1:
                    polyarr.append('-' + variable)
                else:
                    polyarr.append(str(c[1]) + variable)
            elif c[1] == 1:
                polyarr.append(variable + '^' + str(c[0]))
            elif c[1] == -1:
                polyarr.append('-' + variable + '^' + str(c[0]))
            else:
                polyarr.append(str(c[1]) + variable + '^' + str(c[0]))
        return '+'.join(polyarr).replace('+-', '-')

    def evalpoly(self, x):
        # naive evaluation
        # We store partial power values to try and save on computation
        # Much quicker when powers in ascending order
        val = 0
        current_pow = 0
        current_pow_val = 1
        for c in self.coeffpairs:
            if c[0] >= current_pow:
                current_pow_val = current_pow_val * pow(x, c[0] - current_pow)
                current_pow = c[0]
            else:
                current_pow_val = pow(x, c[0])
                current_pow = c[0]
            val += c[1] * current_pow_val
        return val

    def to_dense_poly(self):
        deg = self.degree()
        polyarr = [0 for i in range(deg + 1)]
        for c in self.coeffpairs:
            polyarr[c[0]] = c[1]
        return DensePoly(polyarr)

    def simplify_poly(self):
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
        self.coeffpairs = sorted(new_coeffs, key=lambda x: x[0])


# print("g = SparsePoly([[0,3],[1,5],[6,7]])")
# g = SparsePoly([[0,3],[1,5],[6,7]])
# print(g.degree())
# print(g.printpoly())
# print(g.evalpoly(2))
