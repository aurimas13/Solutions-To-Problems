from sortedcontainers import SortedDict

class MyCalendarTwo:
    def __init__(self):
        self.bookings = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.bookings[start] = self.bookings.get(start, 0) + 1
        self.bookings[end] = self.bookings.get(end, 0) - 1
        
        active_bookings = 0
        for count in self.bookings.values():
            active_bookings += count
            if active_bookings > 2:
                # Revert the changes
                self.bookings[start] -= 1
                self.bookings[end] += 1
                return False
        
        return True