import numpy

N, M = map(int, input().split())
col = []
for _ in range(N):
    col.append(numpy.array(input().strip().split(), int))
print(numpy.transpose(col))
print(numpy.array(col).flatten())

# or

# N, M = map(int, input().split())
# storage = numpy.array([input().strip().split() for _ in range(N)], int)
# print (storage.transpose())
# print (storage.flatten())
