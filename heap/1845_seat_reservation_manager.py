class SeatManager:

    def __init__(self, n: int):
        self.lastSeat = 0
        self.dq = []

    def reserve(self) -> int:
        if not self.dq:
            self.lastSeat += 1
            return self.lastSeat
        return heapq.heappop(self.dq)

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.lastSeat:
            self.lastSeat -= 1
        else:
            heapq.heappush(self.dq, seatNumber)


        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)