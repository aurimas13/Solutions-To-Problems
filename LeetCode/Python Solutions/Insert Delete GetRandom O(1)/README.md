Problem description of "Insert Delete GetRandom O(1)" can be found [here](https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan&id=level-3) and its solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Python%20Solutions/Insert%20Delete%20GetRandom%20O(1)/insert.py).

## Impelmentation:

- Python implementation effectively utilizes a combination of a hash map and a dynamic array to ensure constant time operations on average.
- The critical trick for achieving O(1) removal is to swap the element to be removed with the last element and then pop the last element, thus avoiding the need to shift elements.
- This implementation ensures that `getRandom` has a uniform distribution since each element has an equal probability of being chosen.
