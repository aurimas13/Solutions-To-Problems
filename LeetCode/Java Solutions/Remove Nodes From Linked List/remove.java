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
    public ListNode removeNodes(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        Stack<ListNode> stack = new Stack<>();
        ListNode current = head;
        while (current != null) {
            stack.push(current);
            current = current.next;
        }
        
        int maxVal = Integer.MIN_VALUE;
        ListNode newHead = null;
        while (!stack.isEmpty()) {
            ListNode node = stack.pop();
            if (node.val >= maxVal) {
                maxVal = node.val;
                node.next = newHead;
                newHead = node;
            }
        }
        
        return newHead;
    }
}
