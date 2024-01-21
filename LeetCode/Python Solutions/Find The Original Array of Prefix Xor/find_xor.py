class Solution:
    def findArray(self, pref: 'List[int]') -> 'List[int]':
        n = len(pref)
        arr = [pref[0]]  # for i=0, arr[0] is same as pref[0]
        for i in range(1, n):
            arr.append(pref[i] ^ pref[i-1])
        return arr
