/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        // If the linked list is empty or has only one node, return false.
        if (head == null || head.next == null) {
            return false;
        }
        
        // Initialize two pointers, slow and fast. Slow moves one step at a time and fast moves two steps.
        ListNode slow = head;
        ListNode fast = head.next;
        
        // If there's a cycle, the fast pointer will eventually catch up to the slow pointer.
        while (slow != fast) {
            if (fast == null || fast.next == null) {  // If we reach the end of the list, there's no cycle.
                return false;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // If the loop exits because slow == fast, then there's a cycle.
        return true;
    }
}
