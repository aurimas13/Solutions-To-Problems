# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Initialize the starting nodes for the 'before' and 'after' lists
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head
        
        while head:  # Iterate through the linked list
            # If the current node's value is less than x
            if head.val < x:
                before.next = head  # Add it to the end of the 'before' list
                before = before.next  # Move to the next position
            else:
                after.next = head  # Otherwise, add it to the end of the 'after' list
                after = after.next  # Move to the next position
                
            head = head.next  # Move to the next node in the original list
        
        # At the end, link the 'before' list to the 'after' list
        after.next = None  # Make sure the last node of 'after' list points to None
        before.next = after_head.next  # Linking the two lists
        
        return before_head.next  # Return the combined list starting from the first node

# Time Complexity: O(n) - We iterate through the list once.
# Space Complexity: O(1) - We use constant extra space.
