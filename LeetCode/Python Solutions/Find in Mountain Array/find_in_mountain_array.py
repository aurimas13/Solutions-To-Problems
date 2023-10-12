# Assuming MountainArray is predefined as per the problem

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        # Binary search to find the peak of the mountain
        l, r = 0, mountain_arr.length() - 1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        
        peak = l
        
        # Binary search in the ascending part of the mountain
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            curr_val = mountain_arr.get(mid)
            if curr_val == target:
                return mid
            elif curr_val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # Binary search in the descending part of the mountain
        l, r = peak, mountain_arr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            curr_val = mountain_arr.get(mid)
            if curr_val == target:
                return mid
            elif curr_val < target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
    
    
