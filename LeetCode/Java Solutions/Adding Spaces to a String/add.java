class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder result = new StringBuilder();
        int spaceIndex = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // Add space if current index is in spaces array
            if (spaceIndex < spaces.length && i == spaces[spaceIndex]) {
                result.append(' ');
                spaceIndex++;
            }
            result.append(s.charAt(i));
        }
        
        return result.toString();
    }
}