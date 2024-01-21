class Solution:
    @staticmethod
    def findContestMatch(n: int) -> str:
        teams = [str(i) for i in range(1, n + 1)]
        while n > 1:
            for i in range(n // 2):
                teams[i] = "(" + teams[i] + "," + teams[n - i - 1] + ")"
            n = n // 2
        return teams[0]


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.findContestMatch(n = 4)
    # n = 4 -> ((1,4),(2,3))
    # n = 8 -> (((1,8),(4,5)),((2,7),(3,6)))
    print(Solve)
