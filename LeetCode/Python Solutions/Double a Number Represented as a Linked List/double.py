# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def doubleIt(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        # Reverse the linked list to start from the least significant digit
        head = self.reverse(head)
        
        current = head
        carry = 0
        # Create a dummy node to simplify handling the last node with carry
        dummy = ListNode(0)
        last = dummy
        while current:
            doubled_value = current.val * 2 + carry
            current.val = doubled_value % 10
            carry = doubled_value // 10
            last.next = current
            last = current
            current = current.next
        
        # If there's a carry remaining after the last processed node, add a new node
        if carry:
            last.next = ListNode(carry)
        
        # Reverse the list again to restore the order
        return self.reverse(dummy.next)