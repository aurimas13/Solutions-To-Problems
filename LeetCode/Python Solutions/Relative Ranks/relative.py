from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Sort scores with indices
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        
        # Result array of the same length as scores
        result = [""] * len(score)
        
        # Map sorted positions to their respective ranks
        for rank, (index, _) in enumerate(sorted_scores):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)
        
        return result
