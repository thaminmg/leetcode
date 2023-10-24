import heapq
from collections import defaultdict


# nums = [1, 2, 9, 3, 4, 5, 2, 2, 9, 0, 2, 7, 2]
# print(find_most_frequent_number(nums)) # prints 2

import random
from collections import Counter
import time


def find_most_frequent_number(nums):
    counter = defaultdict(int)
    max_heap = []

    for num in nums:
        counter[num] += 1
        heapq.heappush(max_heap, (-counter[num], num))

    return max_heap[0][1]

n = 1000000
K = 100 

nums = [random.randint(0, K - 1) for _ in range(n)]


# max-heap method
starts = time.time()
result = find_most_frequent_number(nums)
ends = time.time()
print("Using Max-Heap method: result = " + str(result)  + ", time = " + str(ends - starts) + " seconds")

# using Counter dictionary
starts = time.time()
counter = Counter(nums)
result = counter.most_common(1)[0][0]
ends = time.time()
print("Using Python Counter: result = " + str(result)  + ", time " + str(ends - starts) + " seconds")
