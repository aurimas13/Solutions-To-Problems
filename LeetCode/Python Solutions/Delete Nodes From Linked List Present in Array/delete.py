class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a set of numbers to remove
        num_set = set(nums)
        
        # Create a dummy node to handle the case where the head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the list and remove nodes with values in num_set
        while current.next:
            if current.next.val in num_set:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next