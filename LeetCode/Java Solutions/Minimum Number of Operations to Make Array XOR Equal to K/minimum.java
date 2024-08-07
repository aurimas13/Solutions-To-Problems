public class minimum {
    public int minOperations(int[] nums, int k) {
        int currentXor = 0;
        
        // Calculate the initial XOR of all numbers
        for (int num : nums) {
            currentXor ^= num;
        }
        
        // Calculate the required XOR to make the XOR of the array equal to k
        int requiredXor = currentXor ^ k;
        
        // Count the number of 1's in the binary representation of requiredXor
        return Integer.bitCount(requiredXor);
    }
}
