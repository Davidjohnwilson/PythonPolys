#Polynomial classes

#dense polynomial
class DensePoly:
    def __init__(self,coeffs):
        self.coeffs = coeffs
    def degree(self):
        return len(self.coeffs)-1

f = DensePoly([3,2,5])
print(f.degree())

#Sparse Poly
class SparsePoly:
    def __init__(self,coeffpairs):
        self.coeffpairs = coeffpairs

