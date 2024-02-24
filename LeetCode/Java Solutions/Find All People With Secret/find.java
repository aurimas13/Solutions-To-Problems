import java.util.*;

class Solution {
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        // Initialize a set to keep track of people who know the secret
        Set<Integer> knownSet = new HashSet<>();
        knownSet.add(0);
        knownSet.add(firstPerson);
        
        // Sort meetings by time
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[2], b[2]));
        
        // Group meetings by the same time
        List<List<int[]>> sortedMeetings = new ArrayList<>();
        int currentTime = -1;
        for (int[] meeting : meetings) {
            if (meeting[2] != currentTime) {
                sortedMeetings.add(new ArrayList<>());
                currentTime = meeting[2];
            }
            sortedMeetings.get(sortedMeetings.size() - 1).add(new int[]{meeting[0], meeting[1]});
        }
        
        // Iterate over each group of meetings
        for (List<int[]> meetingGroup : sortedMeetings) {
            Set<Integer> peopleKnowSecret = new HashSet<>();
            Map<Integer, List<Integer>> graph = new HashMap<>();
            
            // Build the graph for the current time step and update people who know the secret
            for (int[] meeting : meetingGroup) {
                graph.computeIfAbsent(meeting[0], k -> new ArrayList<>()).add(meeting[1]);
                graph.computeIfAbsent(meeting[1], k -> new ArrayList<>()).add(meeting[0]);
                if (knownSet.contains(meeting[0])) peopleKnowSecret.add(meeting[0]);
                if (knownSet.contains(meeting[1])) peopleKnowSecret.add(meeting[1]);
            }
            
            // BFS to propagate the secret among people in the current time step
            Queue<Integer> queue = new LinkedList<>(peopleKnowSecret);
            while (!queue.isEmpty()) {
                int curr = queue.poll();
                knownSet.add(curr);
                for (int neighbor : graph.get(curr)) {
                    if (!knownSet.contains(neighbor)) {
                        knownSet.add(neighbor);
                        queue.add(neighbor);
                    }
                }
            }
        }
        
        // Convert the set of people who know the secret to a list
        return new ArrayList<>(knownSet);
    }
}
