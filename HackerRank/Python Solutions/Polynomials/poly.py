import numpy

P = numpy.array(list(map(float, input().split())), float)
x = int(input())
print(numpy.polyval(P, x))