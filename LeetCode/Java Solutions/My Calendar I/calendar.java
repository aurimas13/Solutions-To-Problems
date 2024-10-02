import java.util.TreeMap;

class MyCalendar {
    private TreeMap<Integer, Integer> bookings;

    public MyCalendar() {
        bookings = new TreeMap<>();
    }
    
    public boolean book(int start, int end) {
        // Check if there's an event that ends after this event starts
        Integer prevStart = bookings.floorKey(start);
        if (prevStart != null && bookings.get(prevStart) > start) {
            return false;
        }
        
        // Check if there's an event that starts before this event ends
        Integer nextStart = bookings.ceilingKey(start);
        if (nextStart != null && nextStart < end) {
            return false;
        }
        
        // If no conflict, add the event
        bookings.put(start, end);
        return true;
    }
}