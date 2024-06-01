/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        // Step 1: Copy the value from the next node to the current node
        node.val = node.next.val;
        
        // Step 2: Remove the next node from the list by skipping it
        node.next = node.next.next;
    }
}
