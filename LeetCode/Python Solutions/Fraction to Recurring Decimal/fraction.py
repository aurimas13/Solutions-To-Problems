import collections


class Solution:
    @staticmethod
    def fractionToDecimal(numerator: int, denominator: int) -> str:
        if not numerator:
            return "0"

        res = []

        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        dividend, divisor = abs(numerator), abs(denominator)
        # q = quotient, r = remainder
        q, r = divmod(dividend, divisor)
        res.append(str(q))

        if not r:
            return "".join(res)

        res.append(".")
        indices = collections.defaultdict(int)

        while r and r not in indices:
            indices[r] = len(res)
            q, r = divmod(r * 10, divisor)
            res.append(str(q))

        if r in indices:
            res.insert(indices[r], "(")
            res.append(")")

        return "".join(res)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.fractionToDecimal(numerator = 2, denominator = 1)
    # numerator = 2, denominator = 1 -> "2" | numerator = 1, denominator = 2 -> "0.5" |
    # numerator = 4, denominator = 333 -> "0.(012)"
    print(Solve)
