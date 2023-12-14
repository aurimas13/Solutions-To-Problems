import numpy

N, M = map(int, input().split())
# for _ in range(N): # gives a list
A = numpy.array([list(map(int, input().split())) for _ in range(N)]) # gives a list of list
B = numpy.array([list(map(int, input().split())) for _ in range(N)]) # gives a list of list
print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.floor_divide(A,B))
print(numpy.mod(A,B))
print(numpy.power(A,B))
