import numpy

N = int(input())
A = numpy.array([list(map(int, input().split())) for _ in range(N)], int)
B = numpy.array([list(map(int, input().split())) for _ in range(N)], int)
print(numpy.dot(A, B))