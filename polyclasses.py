#Polynomial classes

#dense polynomial
class DensePoly:
    'Polynomials stored in a dense manner'
    coeffs = []
    
    def __init__(self,coeffs):
        self.coeffs = coeffs
    def degree(self):
        return len(self.coeffs)-1
    def printpoly(self):
        polystr = ''
        n=len(self.coeffs)
        for i in xrange(1,n):
            print i
            polystr += str(self.coeffs[n-i])
            polystr += 'x^'+str(n-i) + '+'
        polystr += str(self.coeffs[0])
        return polystr

f = DensePoly([3,2,5])
print(f.degree())
print(f.printpoly())

#Sparse Poly
class SparsePoly:
    'Polynomials stored in a sparse manner'
    coeffpairs=[]

    def __init__(self,coeffpairs):
        self.coeffpairs = coeffpairs
    
    def degree(self):
        deg = 0
        for i in xrange(len(self.coeffpairs)):
            if self.coeffpairs[i][0] > deg:
                deg = self.coeffpairs[i][0]
        return deg

g = SparsePoly([[0,3],[1,5],[6,7]])
print(g.degree())
