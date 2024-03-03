class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize a dummy node to simplify edge cases like removing the head
        dummy = ListNode(0, head)
        slow = fast = dummy
        
        # Advance fast pointer n steps ahead
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # Skip the target node
        slow.next = slow.next.next
        
        return dummy.next  # Return head of the modified list
