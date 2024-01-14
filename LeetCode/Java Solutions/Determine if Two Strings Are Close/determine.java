class Solution {
    public boolean halvesAreAlike(String s) {
        int mid = s.length() / 2, vowelCount1 = 0, vowelCount2 = 0;
        String vowels = "aeiouAEIOU";

        for (int i = 0; i < mid; i++) {
            if (vowels.indexOf(s.charAt(i)) >= 0) {
                vowelCount1++;
            }
            if (vowels.indexOf(s.charAt(i + mid)) >= 0) {
                vowelCount2++;
            }
        }

        return vowelCount1 == vowelCount2;
    }
}

