import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> taskFrequencies = tasksToMap(tasks);
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        maxHeap.addAll(taskFrequencies.values());
        
        int maxFrequency = maxHeap.poll();
        int maxIdleTime = (maxFrequency - 1) * n;
        
        while (!maxHeap.isEmpty()) {
            maxIdleTime -= Math.min(maxFrequency - 1, maxHeap.poll());
        }
        
        maxIdleTime = Math.max(0, maxIdleTime);
        return tasks.length + maxIdleTime;
    }

    private Map<Character, Integer> tasksToMap(char[] tasks) {
        Map<Character, Integer> dic = new HashMap<>();
        for (char task : tasks) {
            dic.put(task, dic.getOrDefault(task, 0) + 1);
        }
        return dic;
    }

    public static void main(String[] args) {
        Solution instant = new Solution();
        int solve = instant.leastInterval(new char[]{'A', 'A', 'A', 'B', 'B', 'B'}, 2);
        System.out.println(solve);  // Expected output: 8
    }
}
