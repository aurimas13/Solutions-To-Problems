public class reverse {
    public String reversePrefix(String word, char ch) {
        // Find the index of the first occurrence of ch
        int index = word.indexOf(ch);
        
        // If ch is not found, return the original word
        if (index == -1) {
            return word;
        }
        
        // Reverse the substring from start to index (inclusive)
        StringBuilder reversed = new StringBuilder(word.substring(0, index + 1));
        reversed.reverse();
        
        // Concatenate the reversed substring with the rest of the word
        return reversed.toString() + word.substring(index + 1);
    }
}
