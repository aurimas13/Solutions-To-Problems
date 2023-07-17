# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # two stacks to hold the nodes of two linked lists
        s1, s2 = [], []
        
        # traverse through the linked lists and push the nodes to the stacks
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        sum = 0
        # a new linked list to hold the result
        result = ListNode(0)
        
        # calculate the sum
        while s1 or s2:
            if s1: 
                sum += s1.pop()
            if s2: 
                sum += s2.pop()
            # store the result in a new node
            result.val = sum % 10
            # create a new node for the carry if there is
            head = ListNode(sum // 10)
            head.next = result
            result = head
            # update the sum
            sum //= 10
            
        return result.next if result.val == 0 else result



