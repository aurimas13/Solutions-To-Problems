from typing import List


class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        arr=[]
        c=0
        i=0
        while(i<len(nums)):
            if(nums[i]==0):
                c=0
            else:
                c+=1
            i+=1
            arr.append(c)
        return max(arr)


# Checking in PyCharm/terminal
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1])
    # nums = [1,0,1,1,0,1] -> 2
    # nums = [1,1,0,1,1,1] -> 3
    print(Solve)
