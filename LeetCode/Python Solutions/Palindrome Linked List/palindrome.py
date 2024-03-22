# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Find the middle of the list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half
        second_half_head = self.reverse(slow.next)
        first_half_head = head
        
        # Compare the first and second half nodes
        result = True
        while result and second_half_head:
            if first_half_head.val != second_half_head.val:
                result = False
            first_half_head = first_half_head.next
            second_half_head = second_half_head.next
        
        # Restore the list (optional)
        slow.next = self.reverse(slow.next)
        
        return result
    
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next_temp = head.next
            head.next = prev
            prev = head
            head = next_temp
        return prev
  