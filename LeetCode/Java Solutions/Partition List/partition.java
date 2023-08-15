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
    public ListNode partition(ListNode head, int x) {
        // Initialize the starting nodes for the 'before' and 'after' lists
        ListNode beforeHead = new ListNode(0);
        ListNode before = beforeHead;
        ListNode afterHead = new ListNode(0);
        ListNode after = afterHead;
        
        while (head != null) {  // Iterate through the linked list
            // If the current node's value is less than x
            if (head.val < x) {
                before.next = head;  // Add it to the end of the 'before' list
                before = before.next;  // Move to the next position
            } else {
                after.next = head;  // Otherwise, add it to the end of the 'after' list
                after = after.next;  // Move to the next position
            }
            
            head = head.next;  // Move to the next node in the original list
        }
        
        // At the end, link the 'before' list to the 'after' list
        after.next = null;  // Make sure the last node of 'after' list points to null
        before.next = afterHead.next;  // Linking the two lists
        
        return beforeHead.next;  // Return the combined list starting from the first node
    }
}

// Time Complexity: O(n) - We iterate through the list once.
// Space Complexity: O(1) - We use constant extra space.
