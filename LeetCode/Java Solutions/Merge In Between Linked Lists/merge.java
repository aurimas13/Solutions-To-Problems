class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    // Updated deserialize method to handle input strings with brackets
    public static ListNode deserialize(String data) {
        // Remove brackets and any whitespace characters
        data = data.replaceAll("[\\[\\]\\s]", "");
        if (data.isEmpty()) {
            return null;
        }
        String[] parts = data.split(",");
        ListNode head = new ListNode(Integer.parseInt(parts[0]));
        ListNode current = head;
        for (int i = 1; i < parts.length; i++) {
            current.next = new ListNode(Integer.parseInt(parts[i]));
            current = current.next;
        }
        return head;
    }
}

class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        // Find the node before the a-th node
        ListNode nodeBeforeA = list1;
        for (int i = 0; i < a - 1; i++) {
            nodeBeforeA = nodeBeforeA.next;
        }
        
        // Find the b-th node
        ListNode nodeB = nodeBeforeA;
        for (int i = 0; i < b - a + 2; i++) {
            nodeB = nodeB.next;
        }
        
        // Connect the end of list1 to the beginning of list2
        nodeBeforeA.next = list2;
        
        // Find the end of list2
        ListNode nodeEndOfList2 = list2;
        while (nodeEndOfList2.next != null) {
            nodeEndOfList2 = nodeEndOfList2.next;
        }
        
        // Connect the end of list2 to the node after the b-th node
        nodeEndOfList2.next = nodeB;
        
        return list1;
    }
}
