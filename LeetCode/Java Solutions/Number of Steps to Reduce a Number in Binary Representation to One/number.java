class Solution {
    public int numSteps(String s) {
        int steps = 0;
        int carry = 0;
        
        // Start from the least significant bit and move to the most significant bit
        for (int i = s.length() - 1; i > 0; i--) {
            if ((s.charAt(i) - '0') + carry == 1) {
                // If the current bit + carry is 1, it's odd, so we need to add 1
                carry = 1;  // This effectively becomes carry for the next higher bit
                steps += 2;  // 1 for addition and 1 for division
            } else {
                // If the current bit + carry is 0, it's even, so we just divide by 2
                steps += 1;
            }
        }
        
        // If there's a carry after processing all bits except the leftmost one
        return steps + carry;
    }

    // Test the solution
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.numSteps("1101"));  // Output: 6
        System.out.println(sol.numSteps("10"));    // Output: 1
        System.out.println(sol.numSteps("1"));     // Output: 0
    }
}
