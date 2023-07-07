import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public long totalCost(int[] quality, int k, int candidates) {
        long totalCost = 0;
        
        PriorityQueue<AbstractMap.SimpleEntry<Integer, Integer>> minHeap1 = new PriorityQueue<>(Comparator.comparing(AbstractMap.SimpleEntry::getValue));
        PriorityQueue<AbstractMap.SimpleEntry<Integer, Integer>> minHeap2 = new PriorityQueue<>(Comparator.comparing(AbstractMap.SimpleEntry::getValue));
        
        List<AbstractMap.SimpleEntry<Integer, Integer>> workers = new ArrayList<>();
        
        int left = 0;
        int right = quality.length - 1;
        int removed = 0;
        
        for (int i = 0; i < quality.length; i++) {
            workers.add(new AbstractMap.SimpleEntry<>(i, quality[i]));
        }
        
        while (k > 0 && 2 * candidates < workers.size() - removed) {
            while (minHeap1.size() < candidates) {
                minHeap1.add(workers.get(left));
                left++;
            }
            
            while (minHeap2.size() < candidates) {
                minHeap2.add(workers.get(right));
                right--;
            }
            
            AbstractMap.SimpleEntry<Integer, Integer> worker1 = minHeap1.peek();
            AbstractMap.SimpleEntry<Integer, Integer> worker2 = minHeap2.peek();
            
            if (worker1.getValue() < worker2.getValue()) {
                totalCost += worker1.getValue();
                k--;
                minHeap1.poll();
                removed++;
            } else if (worker1.getValue() > worker2.getValue()) {
                totalCost += worker2.getValue();
                k--;
                minHeap2.poll();
                removed++;
            } else {
                if (worker1.getKey() < worker2.getKey()) {
                    totalCost += worker1.getValue();
                    k--;
                    minHeap1.poll();
                    removed++;
                } else {
                    totalCost += worker2.getValue();
                    k--;
                    minHeap2.poll();
                    removed++;
                }
            }
        }
        
        minHeap1.addAll(minHeap2);
        
        while (left <= right) {
            minHeap1.add(workers.get(left));
            left++;
        }
        
        while (k > 0) {
            AbstractMap.SimpleEntry<Integer, Integer> worker = minHeap1.poll();
            totalCost += worker.getValue();
            k--;
        }
        
        return totalCost;
    }
}
