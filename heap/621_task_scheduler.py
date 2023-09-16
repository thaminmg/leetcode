class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        queue = collections.deque()
        hset = {}
        count = 0   
        for task in tasks:
            if task in hset:
                hset[task] += 1
            else:
                hset[task] = 1

        for task in hset:
            heapq.heappush(maxHeap, -hset[task])

        while maxHeap or queue:
            count += 1
            if maxHeap:
                remaining = heapq.heappop(maxHeap)
                remaining = -remaining - 1
                if remaining:
                    queue.append((remaining, count + n))

            if queue and queue[0][1] == count:
                heapq.heappush(maxHeap, - queue.popleft()[0])

        return count

        
