class Solution:
    @staticmethod
    def intToRoman(num: int) -> str:
        decToRoman = {
            1000:'M',900:'CM',
            500:'D', 400:'CD',
            100:'C',90:'XC',
            50:'L', 40:'XL',
            10:'X', 9:'IX',
            5:'V', 4:'IV', 1:'I'
                     }
        roman_str = ''
        for key, val in decToRoman.items():
            while num >= key:
                num = num - key
                roman_str = roman_str+val
        return roman_str


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.intToRoman(num=58)  # num = 58 -> LVIII | num = 3 -> III
    print(Solve)
