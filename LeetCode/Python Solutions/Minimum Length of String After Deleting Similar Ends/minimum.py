class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            ch = s[left]
            # Move left pointer to the right past all characters equal to ch
            while left <= right and s[left] == ch:
                left += 1
            # Move right pointer to the left past all characters equal to ch
            while right >= left and s[right] == ch:
                right -= 1
                
        # Return the length of the remaining string
        return right - left + 1
