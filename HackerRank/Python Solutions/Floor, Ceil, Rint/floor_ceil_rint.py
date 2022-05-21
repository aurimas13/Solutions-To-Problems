import numpy

numpy.set_printoptions(sign=' ')
N = numpy.array(input().split(), float)
print(numpy.floor(N))
print(numpy.ceil(N))
print(numpy.rint(N))

# Wrong because of spacing for the answer yet the answer is correct:
#
# N = numpy.array(list(map(float, input().split())))
# print(numpy.floor(N))
# print(numpy.ceil(N))
# print(numpy.rint(N))