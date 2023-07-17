import java.util.ArrayDeque;
import java.util.Deque;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    // Deserialize a comma separated string into a ListNode
    public static ListNode deserialize(String data) {
        // Remove unwanted characters such as brackets or spaces
        data = data.replaceAll("[\\[\\] ]", "");
        String[] values = data.split(",");
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        for (String value : values) {
            current.next = new ListNode(Integer.parseInt(value.trim()));
            current = current.next;
        }
        return dummy.next;
    }
}

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // two stacks to hold the nodes of two linked lists
        Deque<Integer> s1 = new ArrayDeque<>();
        Deque<Integer> s2 = new ArrayDeque<>();

        // traverse through the linked lists and push the nodes to the stacks
        while (l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }

        int sum = 0;
        ListNode result = new ListNode(0);
        while (!s1.isEmpty() || !s2.isEmpty()) {
            if (!s1.isEmpty()) sum += s1.pop();
            if (!s2.isEmpty()) sum += s2.pop();
            // store the result in a new node
            result.val = sum % 10;
            // create a new node for the carry if there is
            ListNode head = new ListNode(sum / 10);
            head.next = result;
            result = head;
            // update the sum
            sum /= 10;
        }

        return result.val == 0 ? result.next : result;
    }

    public static void main(String[] args) {
        // Assuming you have two strings representing linked lists
        String list1 = "7,2,4,3";
        String list2 = "5,6,4";
        
        // Create ListNode instances from the strings
        ListNode l1 = ListNode.deserialize(list1);
        ListNode l2 = ListNode.deserialize(list2);
        
        // Create a Solution instance and use it to add the two numbers
        Solution solution = new Solution();
        ListNode result = solution.addTwoNumbers(l1, l2);
        
        // Output the result
        while (result != null) {
            System.out.print(result.val + " ");
            result = result.next;
        }
    }
}


