from collections import heapq as hq
class MyCalendar:
    booked = None
    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for r_start, r_end in self.booked:
            if (start <= r_start and end > r_start) or (start >= r_start and start < r_end):
                return False
        self.booked.append([start, end])
        return True

