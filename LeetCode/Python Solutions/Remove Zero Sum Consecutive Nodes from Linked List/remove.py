class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        # Dictionary to store the last node for each prefix sum
        prefixSum = {0: dummy}
        sumSoFar = 0
        
        # First pass to build the prefix sum map
        current = head
        while current:
            sumSoFar += current.val
            prefixSum[sumSoFar] = current
            current = current.next
        
        # Second pass to remove zero sum sublists
        sumSoFar = 0
        current = dummy
        while current:
            sumSoFar += current.val
            # Connect to the last node of the same running sum encountered
            current.next = prefixSum[sumSoFar].next
            current = current.next
        
        return dummy.next