class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flight = defaultdict(list)

        for origin, destination in tickets:
            self.flight[origin].append(destination)
        
        for origin, itinerary in self.flight.items():
            itinerary.sort(reverse = True)

        self.res = []
        self.dfs('JFK')

        return self.res[::-1]

    def dfs(self, origin):
        destinations = self.flight[origin]

        while destinations:
            next_destination = destinations.pop()
            self.dfs(next_destination)

        self.res.append(origin)
        