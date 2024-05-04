import java.util.Arrays;

class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int left = 0, right = people.length - 1;
        int boats = 0;
        
        while (left <= right) {
            if (people[left] + people[right] <= limit) {
                left++;  // Pair the lightest and heaviest person that can fit together
            }
            right--;  // Heaviest always gets on a boat, either alone or paired
            boats++;
        }
        
        return boats;
    }
}
