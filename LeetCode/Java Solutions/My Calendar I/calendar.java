import java.util.*;

class MyCalendarTwo {
    private TreeMap<Integer, Integer> bookings;

    public MyCalendarTwo() {
        bookings = new TreeMap<>();
    }
    
    public boolean book(int start, int end) {
        bookings.put(start, bookings.getOrDefault(start, 0) + 1);
        bookings.put(end, bookings.getOrDefault(end, 0) - 1);
        
        int activeBookings = 0;
        for (int count : bookings.values()) {
            activeBookings += count;
            if (activeBookings > 2) {
                // Revert the changes
                bookings.put(start, bookings.get(start) - 1);
                bookings.put(end, bookings.get(end) + 1);
                return false;
            }
        }
        
        return true;
    }
}