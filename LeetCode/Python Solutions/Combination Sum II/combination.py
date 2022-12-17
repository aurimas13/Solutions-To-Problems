from typing import List
import collections
import copy


class Solution:
    def DFS(self,target,path,recoder):
        if target == 0:
            self.res.append(path)
        else:
            for key in recoder:
                if recoder[key] > 0 and target - key >= 0:
                    recoder_copy = copy.copy(recoder)
                    recoder[key] = 0
                    recoder_copy[key] -= 1
                    self.DFS(target - key,path+[key],recoder_copy)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        recoder = collections.Counter(candidates)
        self.res = []
        self.DFS(target,[],recoder)
        return self.res


# Checking in PyCharm/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
    # candidates = [10,1,2,7,6,1,5], target = 8
    # candidates = [2,5,2,1,2], target = 5
    print(Solve)
