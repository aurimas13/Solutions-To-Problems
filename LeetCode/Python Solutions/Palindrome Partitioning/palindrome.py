from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int, path: List[str], result: List[List[str]]):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path, result)
                    path.pop()
        
        result = []
        backtrack(0, [], result)
        return result

# Example usage
sol = Solution()
print(sol.partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
print(sol.partition("a"))    # Output: [["a"]]
