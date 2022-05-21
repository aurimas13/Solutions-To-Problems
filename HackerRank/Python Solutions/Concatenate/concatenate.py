import numpy

N, M, P = map(int, input().split())
col1, col2 = [], []
for _ in range(N):
    col1.append(numpy.array(input().strip().split(), int))
for _ in range(M):
    col2.append(numpy.array(input().strip().split(), int))
print(numpy.concatenate((col1, col2), axis=0))
