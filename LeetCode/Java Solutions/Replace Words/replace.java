import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children;
    boolean isWord;
    
    public TrieNode() {
        children = new HashMap<>();
        isWord = false;
    }
}

class Trie {
    TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isWord = true;
    }
    
    public String searchRoot(String word) {
        TrieNode node = root;
        StringBuilder prefix = new StringBuilder();
        for (char c : word.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return word;
            }
            node = node.children.get(c);
            prefix.append(c);
            if (node.isWord) {
                return prefix.toString();
            }
        }
        return word;
    }
}

class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        Trie trie = new Trie();
        for (String root : dictionary) {
            trie.insert(root);
        }
        
        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();
        for (String word : words) {
            if (result.length() > 0) {
                result.append(" ");
            }
            result.append(trie.searchRoot(word));
        }
        
        return result.toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.replaceWords(Arrays.asList("cat", "bat", "rat"), "the cattle was rattled by the battery"));  // Output: "the cat was rat by the bat"
        System.out.println(sol.replaceWords(Arrays.asList("a", "b", "c"), "aadsfasf absbs bbab cadsfafs"));  // Output: "a a b c"
    }
}
