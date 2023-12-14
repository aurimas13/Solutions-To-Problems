import numpy

N, M = map(int, input().strip().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(numpy.around(numpy.std(arr, axis = None), decimals=11))