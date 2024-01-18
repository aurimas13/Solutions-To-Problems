import math
class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci formula
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        return int((pow(phi, n + 1) - pow(psi, n + 1)) / sqrt5)

        # Dynamic programming and Fibonacci approach

        # if n == 0: return 0
        # elif n == 1: return 1
        # elif n == 2: return 2
        # else:
        #     temp_1, temp_2 = 1, 2
        #     output = 3
        #     for i in range(2, n):
        #         output = temp_1 + temp_2
        #         temp_1 = temp_2
        #         temp_2 = output
        #     return output

        # if n == 0: return 0
        # if n == 1: return 1
        # if n == 2: return 2
        # else:
        #     first = 1;
        #     second = 2;
        #     for i in range(2, n):
        #         third = first + second
        #         first = second
        #         second = third
        #     return second


# Checking in PyCharm/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.climbStairs(3)  # 3 -> 3 | 6 -> 13
    print(Solve)