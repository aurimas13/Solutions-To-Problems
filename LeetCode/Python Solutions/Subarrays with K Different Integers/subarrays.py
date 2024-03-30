def atMostK(A, K):
    count = {}
    i = res = 0
    for j in range(len(A)):
        if A[j] not in count:
            K -= 1
            count[A[j]] = 0
        count[A[j]] += 1
        while K < 0:
            count[A[i]] -= 1
            if count[A[i]] == 0:
                del count[A[i]]
                K += 1
            i += 1
        res += j - i + 1
    return res

class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return atMostK(nums, k) - atMostK(nums, k-1)
