class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Create a sorted set of unique elements
        sorted_set = sorted(set(arr))
        
        # Create a map to store ranks
        rank_map = {num: rank for rank, num in enumerate(sorted_set, 1)}
        
        # Replace elements with their ranks
        return [rank_map[num] for num in arr]