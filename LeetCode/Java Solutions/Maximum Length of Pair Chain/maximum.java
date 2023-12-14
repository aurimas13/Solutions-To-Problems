from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # Sort pairs by their end element
        curr_end, count = float('-inf'), 0
        
        for pair in pairs:
            # Check if the current pair can be added to the chain
            if curr_end < pair[0]:
                curr_end = pair[1]
                count += 1
                
        return count
