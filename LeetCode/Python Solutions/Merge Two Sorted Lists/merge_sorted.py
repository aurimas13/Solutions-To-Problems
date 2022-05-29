# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        return sorted(list1 + list2)


# Instantiation of the class to check the values
if __name__ == '__main__':
    Solve = Solution.mergeTwoLists(1, [1,2,4], [1,3,4])
    print(Solve)