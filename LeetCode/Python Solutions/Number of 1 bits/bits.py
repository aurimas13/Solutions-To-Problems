class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# if __name__ == '__main__':
#     Instant = Solution()
#     Solve = Instant.hammingWeight(int(00000000000000000000000000001011))
#     print(Solve)

# Playground
# n = '00000000000000000000000000001011'
# print(bin(int(n)).count('1'))