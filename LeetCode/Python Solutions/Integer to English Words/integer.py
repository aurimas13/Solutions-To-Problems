from collections import deque


class Solution:
    @staticmethod
    def numberToWords(num: int) -> str:
        dic = {
            1000000000: "Billion",
            1000000: "Million",
            1000: "Thousand",
            100: "Hundred",
            90: "Ninety",
            80: "Eighty",
            70: "Seventy",
            60: "Sixty",
            50: "Fifty",
            40: "Forty",
            30: "Thirty",
            20: "Twenty",
            19: "Nineteen",
            18: "Eighteen",
            17: "Seventeen",
            16: "Sixteen",
            15: "Fifteen",
            14: "Fourteen",
            13: "Thirteen",
            12: "Twelve",
            11: "Eleven",
            10: "Ten",
            9: "Nine",
            8: "Eight",
            7: "Seven",
            6: "Six",
            5: "Five",
            4: "Four",
            3: "Three",
            2: "Two",
            1: "One",
            0: "Zero",
        }
        if num == 0: return dic[0]

        segments = [float("inf"), 1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20]

        def numberToWords(number):
            nonlocal dic, segments
            ret = deque()
            for i in range(1, len(segments)):
                if segments[i] <= number < segments[i - 1]:
                    div, rest = number // segments[i], number % segments[i]
                    ret.append(dic[segments[i]])
                    if rest > 0: ret.append(numberToWords(rest))
                    # We say "One Hundred", "One thoushand" but we don't say "One Fifty", we simply say "Fifty":
                    if div > 0 and i < 5: ret.appendleft(numberToWords(div))
                    return " ".join(ret)
            return dic[number]

        return numberToWords(num)


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.numberToWords(num = 12345)  # num = 12345 -> "Twelve Thousand Three Hundred Forty Five" | num =
    # 123 -> "One Hundred Twenty Three"
    print(Solve)
