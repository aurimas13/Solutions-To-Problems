import numpy
N, M = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(M)]) 
arr_sum = numpy.sum(arr, axis = 0)
print(numpy.prod(arr_sum))