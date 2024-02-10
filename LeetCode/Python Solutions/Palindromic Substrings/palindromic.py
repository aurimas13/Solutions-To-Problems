class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromesAroundCenter(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        totalPalindromes = 0
        for i in range(len(s)):
            # Odd-length palindromes, centered at i
            totalPalindromes += countPalindromesAroundCenter(i, i)
            # Even-length palindromes, centered between i and i+1
            totalPalindromes += countPalindromesAroundCenter(i, i + 1)
        
        return totalPalindromes

