# coding: utf-8
from __future__ import division

#Polynomial classes
from math import *

#dense polynomial
#We store an array with all the coefficients for every degree
class DensePoly:
    'Polynomials stored in a dense manner'
    coeffs = []
    
    def __init__(self,coeffs):

        tmp_coeffs = coeffs
        while tmp_coeffs and (tmp_coeffs[-1]==0):
            tmp_coeffs.pop()
        self.coeffs = tmp_coeffs

    def degree(self):
        #degree is just the length of the vector of coefficients minus 1 
        #(as we store the 0 coefficient
        if len(self.coeffs)==0:
            return 0
        else:
            return len(self.coeffs)-1


    def printpoly(self,variable='x'):
        #Printing polynomial with placeholder 'x'
        polyarr = []
        dummy_variable = variable
        n=len(self.coeffs)
        if n == 0:
            return ''
        for i in xrange(1,n-1):
            #we work backwards
            if self.coeffs[n-i] != 0:
                polyarr.append(str(self.coeffs[n-i])+dummy_variable+'^'+str(n-i))
        if n>0 and self.coeffs[1] != 0:
            polyarr.append(str(self.coeffs[1])+dummy_variable)
        if self.coeffs[0] != 0:
            polyarr.append(str(self.coeffs[0]))
        return '+'.join(polyarr)



    def evalpoly(self,x):
        #naive evaluation
        val = 0
        for i in xrange(len(self.coeffs)):
            val += self.coeffs[i]*pow(x,i)
        return val

# print("f = DensePoly([3,2,5]):")
# f = DensePoly([3,2,5])
# print(f.degree())
# print(f.printpoly())
# print(f.evalpoly(2))

#Sparse Poly
class SparsePoly:
    'Polynomials stored in a sparse manner'
    coeffpairs=[]

    def __init__(self,coeffpairs):
        self.coeffpairs = coeffpairs
    
    def degree(self):
        #to check degree we look for largest degree
        deg = 0
        #don't assume all in order!
        for i in xrange(len(self.coeffpairs)):
            if self.coeffpairs[i][0] > deg:
                deg = self.coeffpairs[i][0]
        return deg

    def printpoly(self):
        #print polynomial
        polystr = ''
        n=len(self.coeffpairs)
        for i in xrange(1,n+1):
            if self.coeffpairs[n-i][0]==0:
                polystr += str(self.coeffpairs[n-i][1]) + '+'
            else:
                polystr += str(self.coeffpairs[n-i][1]) + 'x^' + str(self.coeffpairs[n-i][0]) + '+'
        return polystr[:-1]

    def evalpoly(self,x):
        #naive evaluation
        val = 0
        for i in xrange(len(self.coeffpairs)):
            val += self.coeffpairs[i][1]*pow(x,self.coeffpairs[i][0])
        return val
        
# print("g = SparsePoly([[0,3],[1,5],[6,7]])")
# g = SparsePoly([[0,3],[1,5],[6,7]])
# print(g.degree())
# print(g.printpoly())
# print(g.evalpoly(2))
