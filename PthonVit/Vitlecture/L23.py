print("MATRIX")
import numpy

# two matrices are initialized by value
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])

# add() is used to add matrix
print("Addition of two matrix -->")
print(numpy.add(x, y))

print()

# subtract() is used to subtract two matrices
print("Subtraction of two matrix -->")
print(numpy.subtract(x, y))

print()

# divide() is used to divide matrices
print("Matrix division -->")
print(numpy.divide(x,y))

print()

print("Multiplication of two matrix -->")
print(numpy.multiply(x,y))

print()

print("The dot product of two matrix -->")
print(numpy.dot(x,y))

print()

print("Square root of a matrix -->")
# it gonna put square root of every element
print("Square root of matrix x -->", numpy.sqrt(x))
print("Square root of matrix y -->", numpy.sqrt(y))

print()

print("The summation of elements -->")
print("Summation of all the element of matrix x -->", numpy.sum(x))
print("Summation of all the element of matrix y -->", numpy.sum(y))

print()

print("The column wise summation -->")
print("summation of y matrix -->", numpy.sum(y,axis=0))
print("summation of x matrix -->", numpy.sum(x,axis=0))

print()

print("The row wise summation -->")
print("summation of y matrix -->", numpy.sum(y, axis=1))
print("summation of x matrix -->", numpy.sum(x, axis=1))

print()

# using T to transpose the matrix
print("Matrix transposition -->")
print("Transpose of matrix x -->", x.T)
print("Transpose of matrix y -->", y.T)
