import numpy

arr = list(map(int, input().strip().split()))
print(numpy.reshape(numpy.array(arr), (3,3)))