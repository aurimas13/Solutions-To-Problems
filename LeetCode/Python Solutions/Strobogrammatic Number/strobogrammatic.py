class Solution:
    @staticmethod
    def isStrobogrammatic(num: str) -> bool:
        start, end, legal = 0, len(num) - 1, "01689"
        while start <= end:
            if "".join(sorted(num[start] + num[end])) not in ["00", "11", "88", "69"]:
                return False
            start += 1
            end -= 1
        return True


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isStrobogrammatic(num = "69")
    # num = "69" -> true
    # num = "962" -> false
    print(Solve)
