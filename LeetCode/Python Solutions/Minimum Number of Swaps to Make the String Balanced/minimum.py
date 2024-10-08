class Solution:
    def minSwaps(self, s: str) -> int:
        misplaced = 0
        open_count = 0
        
        for bracket in s:
            if bracket == '[':
                open_count += 1
            else:  # bracket == ']'
                if open_count == 0:
                    misplaced += 1
                else:
                    open_count -= 1
        
        return (misplaced + 1) // 2
    
    