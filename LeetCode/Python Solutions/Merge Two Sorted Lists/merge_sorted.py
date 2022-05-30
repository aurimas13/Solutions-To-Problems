# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        # Check if either of the lists is null
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # Choose head which is smaller of the two lists
        if list1.val < list2.val:
            temp = head = ListNode(list1.val)
            list1 = list1.next
        else:
            temp = head = ListNode(list2.val)
            list2 = list2.next
        # Loop until any of the list becomes null
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            temp = temp.next
        # Add all the nodes in l1, if remaining
        while list1 is not None:
            temp.next = ListNode(list1.val)
            list1 = list1.next
            temp = temp.next
        # Add all the nodes in l2, if remaining
        while list2 is not None:
            temp.next = ListNode(list2.val)
            list2 = list2.next
            temp = temp.next
        return head


# Instantiation of the class to check the values
# if __name__ == '__main__':
#     Solve = Solution.mergeTwoLists(1, [1,2,4], [1,3,4])
#     print(Solve)
