from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for _, i in sorted([x, i] for i, x in enumerate(arr)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for _, i in sorted([-x, i] for i, x in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 2, -1, -1):
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]

        return sum(higher)
    
    # Tests for this solution
    if __name__ == "__main__":
        def test_OddEvenJumps():
            """
            Tests for OddEvenJumps
            """
            solution = Solution()
            assert solution.oddEvenJumps([10,13,12,14,15]) == 2
            assert solution.oddEvenJumps([2,3,1,1,4]) == 3
            assert solution.oddEvenJumps([5,1,3,4,2]) == 3
            assert solution.oddEvenJumps([1,2,3,2,1,4,4,5]) == 6
            assert solution.oddEvenJumps([1,2,3,2,1,4,4,5,6,7,8,9,10]) == 12
            assert solution.oddEvenJumps([1,2,3,2,1,4,4,5,6,7,8,9,10,11,12,13]) == 16
            assert solution.oddEvenJumps([1,2,3,2,1,4,4,5,6,7,8,9,10,11,12,13,14,15]) == 18
            assert solution.oddEvenJumps([1,2,3,2,1,4,4,5,6,7,8,9,10,11,12,13,14,15,16]) == 20
            assert solution.oddEvenJumps([1,2,3,2,1,4,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == 22
            assert solution.oddEvenJumps([1,2,3,2,1,4,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == 24
            assert solution.oddEvenJumps([1,2,3,2,1,4,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == 26
            assert solution.oddEvenJumps([1,2,3,2,1,4,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 28  

        test_OddEvenJumps()
        print("All tests passed successfully.") 