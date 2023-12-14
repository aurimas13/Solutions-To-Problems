# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the linked list is empty or has only one node, return False
        if not head or not head.next:
            return False
        
        # Initialize two pointers, slow and fast. Slow moves one step at a time and fast moves two steps.
        slow, fast = head, head.next
        
        # If there's a cycle, the fast pointer will eventually catch up to the slow pointer.
        while slow != fast:
            if not fast or not fast.next:  # If we reach the end of the list, there's no cycle.
                return False
            slow = slow.next
            fast = fast.next.next
        
        # If the loop exits because slow == fast, then there's a cycle.
        return True


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.hasCycle(ListNode([3,2,0,-4])) #  ListNode([3,2,0,-4]) -> False
    print(Solve)
