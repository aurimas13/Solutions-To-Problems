/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeNodes(ListNode head) {
        // We skip the initial zero node
        ListNode current = head.next;
        
        // Dummy node to start the merged list
        ListNode dummy = new ListNode(0);
        ListNode mergedCurrent = dummy;
        int sumVal = 0;
        
        while (current != null) {
            if (current.val == 0) {
                // We reached a zero, create a new node with the sum
                mergedCurrent.next = new ListNode(sumVal);
                mergedCurrent = mergedCurrent.next;
                sumVal = 0;  // Reset the sum
            } else {
                sumVal += current.val;
            }
            
            current = current.next;
        }
        
        return dummy.next;
    }
}
