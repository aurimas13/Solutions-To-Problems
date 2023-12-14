class Solution:
    @staticmethod
    def valid_number(s):
        if s and s[0] in ["+", "-"]:
            s = s[1:]

        if s.count(".") > 1:
            return False

        return s.replace(".", "").isdigit()

    def valid_e_number(self, number, integer):
        if integer and integer[0] in ["+", "-"]:
            integer = integer[1:]

        return self.valid_number(number) and integer.isdigit()

    def isNumber(self, s: str) -> bool:
        s = s.lower()

        e_count = s.count("e")

        if e_count == 1:
            number, integer = s.split('e')

            return self.valid_e_number(number, integer)

        return self.valid_number(s)


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.valid_number(s = "0" )
    # s = "0" -> true | s = "e" -> false | s = "." -> false
    print(Solve)
