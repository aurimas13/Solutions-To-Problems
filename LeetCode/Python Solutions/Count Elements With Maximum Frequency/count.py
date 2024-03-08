class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter
        # Count the frequency of each element
        freq = Counter(nums)
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Count how many elements have the maximum frequency
        return sum(freq[element] for element in freq if freq[element] == max_freq)
