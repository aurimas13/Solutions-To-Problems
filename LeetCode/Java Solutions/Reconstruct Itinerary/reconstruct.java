class Solution {
    Map<String, PriorityQueue<String>> flights;
    LinkedList<String> path;

    public List<String> findItinerary(List<List<String>> tickets) {
        flights = new HashMap<>();
        path = new LinkedList<>();

        for (List<String> ticket : tickets) {
            flights.putIfAbsent(ticket.get(0), new PriorityQueue<>());
            flights.get(ticket.get(0)).offer(ticket.get(1));
        }

        dfs("JFK");
        return path;
    }

    public void dfs(String departure) {
        PriorityQueue<String> destinations = flights.get(departure);
        
        while (destinations != null && !destinations.isEmpty()) {
            dfs(destinations.poll());
        }
        
        path.addFirst(departure);
    }
}
