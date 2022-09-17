class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if n == 0:
                return 1
            half = fastPow(x, n // 2)

            if n % 2 == 0:  # n is even
                return half * half
            else:  # n is odd
                return half * half * x

        N = n
        if N < 0:
            x = 1 / x;
            N = -N

        return fastPow(x, N)


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.myPow(x = 2.10000, n = 3)  # x = 2.00000, n = -2 ->  0.25 | x = 2.10000, n = 3 -> 9.9.261000000000001
    print(Solve)
