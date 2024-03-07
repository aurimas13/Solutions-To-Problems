# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head  # Initialize both pointers to the start of the list
        
        # Move slow pointer one step and fast pointer two steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast pointer reaches the end, slow pointer will be at the middle
        return slow
