class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0
        current_cost = 0
        left = 0
        
        # Use a sliding window to find the maximum length of valid substring
        for right in range(len(s)):
            current_cost += abs(ord(s[right]) - ord(t[right]))
            
            # If current cost exceeds maxCost, move the left pointer
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            # Update max_length if we found a longer valid substring
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Test the solution
if __name__ == '__main__':
    sol = Solution()
    print(sol.equalSubstring("abcd", "bcdf", 3))  # Output: 3
    print(sol.equalSubstring("abcd", "cdef", 3))  # Output: 1
    print(sol.equalSubstring("abcd", "acde", 0))  # Output: 1
