import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Map<Integer, Integer> preferences = new HashMap<>();
        
        // Count the preferences of the students
        for (int student : students) {
            preferences.put(student, preferences.getOrDefault(student, 0) + 1);
        }
        
        // Iterate through the sandwiches
        for (int sandwich : sandwiches) {
            if (!preferences.containsKey(sandwich) || preferences.get(sandwich) == 0) {
                // If no students prefer this type of sandwich, stop
                break;
            }
            preferences.put(sandwich, preferences.get(sandwich) - 1);
        }
        
        // Return the sum of the remaining preferences
        return preferences.values().stream().mapToInt(Integer::intValue).sum();
    }
}
