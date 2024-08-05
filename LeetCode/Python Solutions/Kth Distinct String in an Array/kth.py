from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Count occurrences of each string
        count = Counter(arr)
        
        # Find the kth distinct string
        distinct_count = 0
        for s in arr:
            if count[s] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return s
        
        # If there are fewer than k distinct strings, return ""
        return ""