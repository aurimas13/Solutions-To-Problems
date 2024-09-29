import java.util.*;

class AllOne {
    private class Node {
        int count;
        Set<String> keys;
        Node prev, next;
        Node(int count) {
            this.count = count;
            this.keys = new HashSet<>();
        }
    }

    private Map<String, Node> keyMap;
    private Node head, tail;

    public AllOne() {
        keyMap = new HashMap<>();
        head = new Node(0);
        tail = new Node(Integer.MAX_VALUE);
        head.next = tail;
        tail.prev = head;
    }
    
    public void inc(String key) {
        if (!keyMap.containsKey(key)) {
            if (head.next.count != 1) {
                addNodeAfter(new Node(1), head);
            }
            head.next.keys.add(key);
            keyMap.put(key, head.next);
        } else {
            Node node = keyMap.get(key);
            Node next = node.next;
            if (next.count != node.count + 1) {
                addNodeAfter(new Node(node.count + 1), node);
            }
            next = node.next;
            next.keys.add(key);
            keyMap.put(key, next);
            removeKeyFromNode(key, node);
        }
    }
    
    public void dec(String key) {
        Node node = keyMap.get(key);
        if (node.count == 1) {
            keyMap.remove(key);
        } else {
            Node prev = node.prev;
            if (prev.count != node.count - 1) {
                addNodeAfter(new Node(node.count - 1), prev);
            }
            prev = node.prev;
            prev.keys.add(key);
            keyMap.put(key, prev);
        }
        removeKeyFromNode(key, node);
    }
    
    public String getMaxKey() {
        return tail.prev.count == 0 ? "" : tail.prev.keys.iterator().next();
    }
    
    public String getMinKey() {
        return head.next.count == Integer.MAX_VALUE ? "" : head.next.keys.iterator().next();
    }

    private void addNodeAfter(Node node, Node prev) {
        node.next = prev.next;
        node.prev = prev;
        prev.next.prev = node;
        prev.next = node;
    }

    private void removeNodeFromList(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void removeKeyFromNode(String key, Node node) {
        node.keys.remove(key);
        if (node.keys.isEmpty()) {
            removeNodeFromList(node);
        }
    }
}