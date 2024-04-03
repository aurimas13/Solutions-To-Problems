class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim(); // Remove leading and trailing spaces
        String[] words = s.split(" ");
        return words[words.length - 1].length();
    }
}
