import random
import math
class HashFamily:
    def __init__(self, n, p):
        if p > n:
            raise ValueError("p must be less than or equal to n")
        
        self.n = n
        self.p = p
        self.S = set(random.sample(range(n), p))

    def hash(self, x):
        # Extract bits from x based on the set S
        bits = [int(x[i]) for i in self.S]        
        # Formulate the p-bit number obtained from S
        result = 0
        for i, bit in enumerate(reversed(bits)):
            result += bit << i
        return result
    # def hash(self, x):
    #     # Convert x to binary and pad with leading zeros
    #     x_bin = format(x, '0' + str(self.n) + 'b')
    #     bits = [x_bin[i] for i in self.S]
    #     return int(''.join(bits), 2)

# n = 6
# p = 2
# h = HashFamily(n=n, p=p)
# print(f"h.S: {h.S}")

# x = "011011"
# hashed_value = h.hash(x)
# print(f"hash({x}) = {hashed_value}")

class BloomFilter:
    def __init__(self, m, k, n):
        # self.m = 2**int(math.log2(m))  # Limit m to be a power of 2
        self.m = m
        # print(f"self.m {self.m}")
        self.k = k
        self.n = n
        self.hash_functions = [HashFamily(n, int(math.log2(self.m))) for _ in range(k)]
        self.bit_array = [0] * self.m

    def insert(self, item):
        for hash_function in self.hash_functions:
            index = hash_function.hash(item) % self.m
            self.bit_array[index] = 1

    def lookup(self, item):
        for hash_function in self.hash_functions:
            index = hash_function.hash(item) % self.m
            if self.bit_array[index] == 0:
                return False
        return True

    def batch_insert(self, items):
        for item in items:
            self.insert(item)

# Example usage
# m = 64  # Size of the Bloom Filter
# k = 3   # Number of hash functions
# n = 8   # Number of bits in an input
# m = 16  # Size of the Bloom Filter
# k = 3   # Number of hash functions
# n = 6   # Number of bits in an input

# bloom_filter = BloomFilter(m, k, n)

# # Inserting elements
# bloom_filter.insert(2)
# bloom_filter.insert(3)
# bloom_filter.insert(9)
# print(bloom_filter.bit_array)
# # Looking up elements
# print(bloom_filter.lookup(2))    # True
# print(bloom_filter.lookup(19))    # False

# bloom_filter.batch_insert([21, 7])
# print(bloom_filter.bit_array)

# print(bloom_filter.lookup(22))    # True
# print(bloom_filter.lookup(7))    # False
            
# Generate S: 10000 random 64-bit numbers
S = [format(random.getrandbits(64), '064b') for _ in range(10000)]
# Simulation
results = []

for m in [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]: #
    for k in [2**i for i in range(int(math.log2(m//2)) + 1)]:# [1, 2, 4, 8, min(32, m//2)]:
        bloom_filter = BloomFilter(m, k, 64)
        for q in [m, 2*m, 4*m, 8*m, 16*m, 32*m, 64*m]: # 
            # Generate q n-bit numbers
            query_numbers = [format(random.getrandbits(64), '064b') for _ in range(q)]

            # Batch insert
            bloom_filter.batch_insert(query_numbers)

            # Generate 1000 random n-bit numbers
            test_numbers = [format(random.getrandbits(64), '064b') for _ in range(1000)]

            # Lookup and calculate false positive rate
            false_positives = sum(bloom_filter.lookup(num) for num in test_numbers)

            # Calculate the proportion of false positives
            false_positive_rate = false_positives / 1000.0

            # Append results
            results.append((m, k, q, false_positive_rate))

# Report results
print("m\tk\tq\tFalse Positive Rate")
for result in results:
    print("\t".join(map(str, result)))