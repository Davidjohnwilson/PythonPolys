# `pypoly` - Python Polynomial Module
 
## David John Wilson

[![Build Status](https://travis-ci.org/Davidjohnwilson/PythonPolys.svg?branch=development)](https://travis-ci.org/Davidjohnwilson/PythonPolys)
[![Coverage Status](https://coveralls.io/repos/github/Davidjohnwilson/PythonPolys/badge.svg?branch=development)](https://coveralls.io/github/Davidjohnwilson/PythonPolys?branch=development)
[![Code Health](https://landscape.io/github/Davidjohnwilson/PythonPolys/master/landscape.svg?style=flat)](https://landscape.io/github/Davidjohnwilson/PythonPolys/master)

This module is intended to implement basic polynomials in python. They will be entirely symbolic computations wherever possible.

Note, this module will be fairly basic and is intended mainly as a learning exercise. If you wish to do true symbolic computation in Python you should check out [SymPy](https://github.com/sympy/sympy) (and think of contributing to the project!).

I am currently working on building this out into a full library. The latest stable version will be in the `development` branch and the aim will be for full documentation and test coverage (the travis-ci status of this branch will be shown in the badge above). The original code (which was in a sort of pseudo-package) will be kept in the `master` branch for now.

### Description of Package

The package currently defines two classes: `DensePoly` and `SparsePoly`. These classes both define polynomials, simply in different representations.

To define a `DensePoly` you provide an array of coefficients, increasing from the constant coefficient, followed by $$x$$, then $$x^2$$ etc. So to define the polynomial $$5x^2+2x+3$$ you would call `DensePoly([3,2,5])`

To define a `SparsePoly` you provide an array of arrays: each inner array provides the degree and coefficient of a term in the polynomial. So to define the polynomial $$7x^6+5x+3$$ you would call `SparsePoly([[0,3],[1,5],[6,7]])`.

*Why is it important to provide two representations?* Often some operations for polynomials are easier or more intuitive in a dense representation. However, dense polynomials can quickly become very memory-intensive and inefficient. For example consider the polynomial $$x^1000000-1$$. In sparse format this is straightforward to define: `SparsePoly([[0,-1],[1000000,1]])`. To define it as a dense polynomial `DensePoly(a)` the array `a` would have to have length 1000001 and only the first and last entries would be non-zero. 

#### Available Methods

Currently the following methods are defined for an instance of `DensePoly`:

* `degree()`
* `printpoly()`
* `evalpoly(x)`
* `to_sparse_poly()`

The following methods are defined for an instance of `SparsePoly`:

* `degree()`
* `printpoly()`
* `evalpoly(x)`
* `to_dense_poly()`
* `simplify_poly()`
* `simplify_poly_inplace()`
* `equal_poly()`
* `not_equal_poly()`
* `copy_poly()`
* `add_poly()`
* `negate_poly()`
* `subtract_poly()`
* `multiply_poly()`
* `divide_poly()`
* `differentiate_poly()`
* `integrate_poly()`
* `definite_integral(a, b)`
* `numeric_solve_poly()`
* `symbolic_solve_poly()`


### More information

If you would like more information regarding this package, please visit my website [davidjw.co.uk](https://www.davidjw.co.uk) or email me [developer [at] davidjw.co.uk](developer@davidjw.co.uk).