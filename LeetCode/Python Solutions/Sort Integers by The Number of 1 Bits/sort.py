class Solution:
    def sortByBits(self, arr: 'List[int]') -> 'List[int]':
        # Helper function to count 1's in binary representation
        def countOnes(num):
            return bin(num).count('1')

        # Sorting using lambda function as custom comparator
        return sorted(arr, key=lambda x: (countOnes(x), x))


