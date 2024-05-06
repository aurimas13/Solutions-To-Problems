class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty or has one node
        if not head or not head.next:
            return head
        
        stack = []
        current = head
        # Push all nodes onto a stack
        while current:
            stack.append(current)
            current = current.next
            
        max_val = float('-inf')
        new_head = None
        # Traverse from the end (using the stack)
        while stack:
            node = stack.pop()
            if node.val >= max_val:
                max_val = node.val
                node.next = new_head
                new_head = node
        
        return new_head
