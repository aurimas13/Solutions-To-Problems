class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        count = 0
        primes = [True] * n

        for i in range(2, int(n ** 0.5) + 1):
            if not primes[i]:
                continue
            # mark all multiplies of i not prime
            for j in range(i * i, n, i):
                primes[j] = False

        for i in range(2, n):
            if primes[i]:
                count += 1

        return count


# Checking in PyCharm:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.countPrimes(n=10)  # n = 10 -> 4
    print(Solve)
