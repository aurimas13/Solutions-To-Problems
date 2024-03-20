# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the node before the a-th node
        node_before_a = list1
        for _ in range(a - 1):
            node_before_a = node_before_a.next
        
        # Find the b-th node
        node_b = node_before_a
        for _ in range(b - a + 2):
            node_b = node_b.next
        
        # Connect the end of list1 to the beginning of list2
        node_before_a.next = list2
        
        # Find the end of list2
        node_end_of_list2 = list2
        while node_end_of_list2.next is not None:
            node_end_of_list2 = node_end_of_list2.next
        
        # Connect the end of list2 to the node after b-th node
        node_end_of_list2.next = node_b
        
        return list1
