public class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        // Use StringBuilder for efficient string concatenation
        StringBuilder concatenatedWord1 = new StringBuilder();
        StringBuilder concatenatedWord2 = new StringBuilder();

        // Append all strings from word1 to concatenatedWord1
        for (String s : word1) {
            concatenatedWord1.append(s);
        }

        // Append all strings from word2 to concatenatedWord2
        for (String s : word2) {
            concatenatedWord2.append(s);
        }

        // Compare the two concatenated strings
        return concatenatedWord1.toString().equals(concatenatedWord2.toString());
    }
}
