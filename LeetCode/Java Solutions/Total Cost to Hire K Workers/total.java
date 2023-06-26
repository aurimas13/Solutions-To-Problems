import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int totalCost(int[] costs, int k, int candidates) {
        if (candidates * 2 >= costs.length) {
            Arrays.sort(costs);
            int sum = 0;
            for (int i = 0; i < k; i++) {
                sum += costs[i];
            }
            return sum;
        } else {
            int pointer1 = candidates - 1;
            int pointer2 = costs.length - candidates;

            int[] arr1 = Arrays.copyOfRange(costs, 0, candidates);
            int[] arr2 = Arrays.copyOfRange(costs, pointer2, costs.length);

            PriorityQueue<Integer> pq1 = new PriorityQueue<>();
            PriorityQueue<Integer> pq2 = new PriorityQueue<>();
            
            for (int cost : arr1) {
                pq1.offer(cost);
            }
            
            for (int cost : arr2) {
                pq2.offer(cost);
            }

            int res = 0;

            for (int i = 0; i < k; i++) {
                if (!pq1.isEmpty() && !pq2.isEmpty()) {
                    if (pq1.peek() <= pq2.peek()) {
                        res += pq1.poll();
                        pointer1 += 1;
                        if (pointer1 < pointer2) {
                            pq1.offer(costs[pointer1]);
                        }
                    } else {
                        res += pq2.poll();
                        pointer2 -= 1;
                        if (pointer1 < pointer2) {
                            pq2.offer(costs[pointer2]);
                        }
                    }
                } else {
                    if (!pq1.isEmpty()) {
                        res += pq1.poll();
                    } else {
                        res += pq2.poll();
                    }
                }
            }

            return res;
        }
    }
}
