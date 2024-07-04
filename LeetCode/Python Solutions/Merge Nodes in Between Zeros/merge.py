# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We skip the initial zero node
        current = head.next
        
        # Dummy node to start the merged list
        dummy = ListNode(0)
        merged_current = dummy
        sum_val = 0
        
        while current:
            if current.val == 0:
                # We reached a zero, create a new node with the sum
                merged_current.next = ListNode(sum_val)
                merged_current = merged_current.next
                sum_val = 0  # Reset the sum
            else:
                sum_val += current.val
            
            current = current.next
        
        return dummy.next
