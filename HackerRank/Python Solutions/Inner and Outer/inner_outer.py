import numpy

A = numpy.array([list(map(int, input().split()))], int)
B = numpy.array([list(map(int, input().split()))], int)
print(int(numpy.inner(A, B)))
print(numpy.outer(A, B))