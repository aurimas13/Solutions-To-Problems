# from collections import deque
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

# Instantiation of the class to check the values in PyCharm
if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    nodes = [ListNode(val=i) for i in l1]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes_two = [ListNode(val=i) for i in l2]
    for i in range(len(nodes_two) - 1):
        nodes[i].next = nodes_two[i + 1]
    s = Solution()
    print(s.mergeTwoLists(nodes[1], nodes_two[2]))

# or
#
# head = sortedList = ListNode()
# while list1 and list2 :
# 	if list1.val <= list2.val :
# 		sortedList.next = list1
# 		list1 = list1.next
# 		sortedList = sortedList.next
#
# 	else :
# 		sortedList.next = list2
# 		list2 = list2.next
# 		sortedList = sortedList.next

# sortedList.next = list1 or list2
# return head.next
