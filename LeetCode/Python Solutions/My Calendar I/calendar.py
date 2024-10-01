class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.bookings:
            if start < j and i < end:
                return False
        self.bookings.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)