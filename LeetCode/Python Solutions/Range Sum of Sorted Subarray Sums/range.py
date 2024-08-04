import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize min-heap with (sum, index, end) for each number
        heap = [(num, i, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        
        result = 0
        for i in range(1, right + 1):
            curr_sum, start, end = heapq.heappop(heap)
            
            if i >= left:
                result = (result + curr_sum) % MOD
            
            if end + 1 < n:
                next_sum = curr_sum + nums[end + 1]
                heapq.heappush(heap, (next_sum, start, end + 1))
        
        return result

