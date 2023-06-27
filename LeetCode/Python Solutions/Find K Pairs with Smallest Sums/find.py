class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        This function takes two lists of integers and an integer k as input and returns a list of k smallest pairs.
        The function accepts three parameters:
            1. nums1 (List[int]): A list of integers.
            2. nums2 (List[int]): A list of integers.
            3. k (int): An integer representing the number of smallest pairs to be returned.
        The function returns a list of k smallest pairs.
        """
        if not nums1 or not nums2:
            return []
        
        heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(heap) < k:
                    heappush(heap, (-nums1[i] - nums2[j], nums1[i], nums2[j]))
                else:
                    if -heap[0][0] > nums1[i] + nums2[j]:
                        heappop(heap)
                        heappush(heap, (-nums1[i] - nums2[j], nums1[i], nums2[j]))
                    else:
                        break
        
        res = []
        while heap:
            _, num1, num2 = heappop(heap)
            res.append([num1, num2])
        
        return res
    