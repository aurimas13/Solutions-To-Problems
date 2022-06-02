import numpy
class Solution:
    def reverseBits(self, n: int) -> int:
        return int('{:032b}'.format(n)[::-1], 2)

#Playgorund in PyCharm:
# n = b'00000010100101000001111010011100'
# arr = numpy.array(''.join(list(reversed(n))))
# arr2 = numpy.array(''.join(reversed(str(n))))
# print(int(str(arr), 2))
# print(arr)
# print(int(arr2))