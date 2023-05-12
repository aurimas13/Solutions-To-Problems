class Solution:
    @staticmethod
    def mirrorReflection(p: int, q: int) -> int:
        # First find the first point whose abscissa is a multiple of p
        k = 1
        while p * k % q != 0: k += 1
        # If it is an even multiple of x
        if k % 2 == 0:
            return 0
        else:
            # Judge the odd multiples and even multiples of p respectively
            r = p * k / q
            if r % 2 == 1: return 1
            if r % 2 == 0: return 2


# Tests:
if __name__ == '__main__':
    # p = 3, q = 1 -> 1
    Solve = Solution.mirrorReflection(3, 1)
    print(Solve)
    
    # p = 2, q = 1 -> 2
    Solve = Solution.mirrorReflection(2, 1)
    print(Solve)

