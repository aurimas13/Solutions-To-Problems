from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Count soldiers for each row and keep track of row index
        counts = [(sum(row), i) for i, row in enumerate(mat)]
        # Sort by number of soldiers and then by index
        sorted_counts = sorted(counts)
        # Extract first k indices
        return [row[1] for row in sorted_counts[:k]]
