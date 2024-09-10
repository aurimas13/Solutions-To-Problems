class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current = head
        while current.next:
            gcd_value = self.gcd(current.val, current.next.val)
            new_node = ListNode(gcd_value, current.next)
            current.next = new_node
            current = new_node.next
        
        return head
    
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a