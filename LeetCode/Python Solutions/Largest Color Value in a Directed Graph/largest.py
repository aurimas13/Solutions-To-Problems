class Solution(object):
    @staticmethod
    def largestNumber(nums) -> str:
        def largest(num1, num2):
            if num1 + num2 >= num2 + num1:
                return 0
            else:
                return 1

        def smallest(num1, num2):
            if num1 + num2 < num2 + num1:
                return 0
            else:
                return 1

        def quicksort(nums_arr):
            if not nums_arr or len(nums_arr) == 1:
                return nums_arr
            pivot = nums_arr.pop()
            greater = [i for i in nums_arr if largest(str(pivot), str(i))]
            less = [i for i in nums_arr if smallest(str(pivot), str(i))]
            return quicksort(greater) + [pivot] + quicksort(less)

        return str(int(''.join(map(str, quicksort(nums)))))


# Checking in PyCharm/terminal
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.largestNumber(nums = [3,30,34,5,9])
    # nums = [10,2] -> '210'
    # nums = [3,30,34,5,9] -> '9534330'"'
    print(Solve)
