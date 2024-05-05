class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Copy the value from the next node to the current node
        node.val = node.next.val
        
        # Skip over the next node, effectively deleting it from the linked list
        node.next = node.next.next
