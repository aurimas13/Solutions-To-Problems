class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);  // Sort the greed factors
        Arrays.sort(s);  // Sort the sizes of the cookies

        int child_i = 0;  // Index for children
        int cookie_j = 0;  // Index for cookies

        while (child_i < g.length && cookie_j < s.length) {
            if (s[cookie_j] >= g[child_i]) {  // If the cookie can satisfy the child's greed
                child_i++;  // Move to the next child
            }
            cookie_j++;  // Move to the next cookie regardless
        }

        return child_i;  // The number of content children
    }
}
