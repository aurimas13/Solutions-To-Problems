import numpy

N = int(input())
A = numpy.array([list(map(float, input().split())) for _ in range(N)])
print(numpy.around(numpy.linalg.det(A), decimals=11))

