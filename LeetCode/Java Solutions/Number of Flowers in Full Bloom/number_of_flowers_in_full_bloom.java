import java.util.*;

public class Solution {
    public int[] fullBloomFlowers(int[][] flowers, int[] people) {
        List<int[]> events = new ArrayList<>();
        
        // Create bloom events
        for (int[] flower : flowers) {
            int start = flower[0];
            int end = flower[1];
            events.add(new int[] {start, 1});  // Bloom starts
            events.add(new int[] {end + 1, -1});  // Bloom ends
        }
        
        // Sort events by time
        Collections.sort(events, (a, b) -> Integer.compare(a[0], b[0]));

        // Calculate flowers in bloom at each event
        int bloomCount = 0;
        Map<Integer, Integer> bloomAtTime = new HashMap<>();
        for (int[] event : events) {
            int time = event[0];
            int change = event[1];
            bloomCount += change;
            bloomAtTime.put(time, bloomCount);
        }

        // For each person, find how many flowers are blooming at their arrival time
        int[] res = new int[people.length];
        for (int i = 0; i < people.length; i++) {
            int time = people[i];
            // Use binary search to find the closest event time <= person's arrival
            int index = binarySearch(events, time);
            if (index == -1) {
                res[i] = 0;
            } else {
                int closestEventTime = events.get(index)[0];
                res[i] = bloomAtTime.get(closestEventTime);
            }
        }
        return res;
    }

    private int binarySearch(List<int[]> events, int time) {
        int left = 0, right = events.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (events.get(mid)[0] <= time) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right >= 0 ? right : -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        
        // Test cases
        System.out.println(Arrays.toString(s.fullBloomFlowers(new int[][]{{1,6},{3,7},{9,12},{4,13}}, new int[]{2,3,7,11})));  // [1,2,2,2]
        System.out.println(Arrays.toString(s.fullBloomFlowers(new int[][]{{1,10},{3,3}}, new int[]{3,3,2})));  // [2,2,1]
    }
}

