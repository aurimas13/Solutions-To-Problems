class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Sort both arrays
        target.sort()
        arr.sort()
        
        # Compare the sorted arrays
        return target == arr