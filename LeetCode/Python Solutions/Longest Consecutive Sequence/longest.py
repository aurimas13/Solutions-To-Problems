from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        cur, res = 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            if nums[i - 1] + 1 == nums[i]:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
        return res


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.longestConsecutive([100,4,200,1,3,2])  # [100,4,200,1,3,2] -> 4 | nums = [0,3,7,2,5,8,4,6,0,1] -> 9
    print(Solve)


# OR

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         hs = set(nums)
#         uf = UnionFind(hs)
#         for num in nums:
#             left = uf.find(num-1)
#             right = uf.find(num+1)
#             if left != None:
#                 uf.union(num, left)
#             if right != None:
#                 uf.union(num, right)
#         longest = 0
#         for key in uf.caps:
#             longest = max(longest, uf.caps[key])
#         return longest

# class UnionFind(object):
#     def __init__(self, vertices):
#         self.ids = {}
#         self.caps = {}
#         for vertex in vertices:
#             self.ids[vertex] = vertex
#             self.caps[vertex] = 1

#     def find(self, key):
#         # loop to find to ultimate root
#         if key not in self.ids:
#             return None
#         cur = key
#         while cur != self.ids[cur]:
#             cur = self.ids[cur]
#         return cur

#     def union(self, p, q):
#         if p not in self.ids or q not in self.ids:
#             return
#         pId = self.find(p)
#         qId = self.find(q)
#         if pId == qId:
#             return
#         # attach to the larger tree
#         if self.caps[pId] < self.caps[qId]:
#             self.ids[pId] = qId
#             self.caps[qId] += self.caps[pId]
#         else:
#             self.ids[qId] = pId
#             self.caps[pId] += self.caps[qId]

