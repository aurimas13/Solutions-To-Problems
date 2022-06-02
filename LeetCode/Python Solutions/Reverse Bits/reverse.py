import numpy
class Solution:
    def reverseBits(self, n: int) -> int:
        return int('{:032b}'.format(n)[::-1], 2)

#Playgorund in PyCharm:
# n = '00000010100101000001111010011100'
# arr = numpy.array(''.join(list(reversed(n))))
# print(int(str(arr), 2))