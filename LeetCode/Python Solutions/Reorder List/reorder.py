class ListNode:
    def __init__(self, val=0, next=None):
<<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>
-        self.val = val
-        self.next = next

class Solution:
+    """
+    @param head: The head of the linked list
+    @return: nothing
+    """
<<<<<<<  2794d946-bfee-4795-b6aa-864d746a96a3  >>>>>>>
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half
        prev, curr = None, slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = None  # Cut off the first half
        
        # Merge two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
