# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Calculate the size of each part
        size, remainder = divmod(length, k)
        
        # Step 3: Split the linked list
        result = []
        current = head
        for i in range(k):
            if current:
                result.append(current)
                for j in range(size + (i < remainder) - 1):  # Add an extra node for the first 'remainder' parts
                    if current:
                        current = current.next
                next_part = current.next if current else None
                if current:
                    current.next = None
                current = next_part
            else:
                result.append(None)
        
        return result
