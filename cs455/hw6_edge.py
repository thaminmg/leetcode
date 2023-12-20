import random
import math
import random
import pandas as pd

class HashFamily:
    def __init__(self, n, p):
        if p > n:
            raise ValueError("p must be less than or equal to n")
        self.n = n
        self.S = random.sample(range(n), p)
        # self.S = [1,2,3]

    def hash(self, x):
        # Convert x to binary and pad with leading zeros
        x_bin = format(x, '0' + str(self.n) + 'b')
        # Extract bits at indices in S
        bits = [x_bin[i] for i in self.S]
        # Formulate the p-bit number and return in decimal
        return int(''.join(bits), 2)
    
# h = HashFamily(n=6, p=2)
# print(h.S)  # Prints the random 2-element subset of {0, 1, 2, 3, 4, 5}

# x = 27  # 011011 in binary
# print(h.hash(x))  # Prints the hash value of x


class BloomFilter:
    def __init__(self, m, k, n):
        self.m = m
        self.k = k
        self.bit_array = [0]*m
        self.hash_functions = [HashFamily(n=n, p=int(math.log2(m))) for _ in range(k)]

    def insert(self, x):
        for i in range(self.k):
            index = self.hash_functions[i].hash(x) % self.m
            self.bit_array[index] = 1

    def lookup(self, x):
        for i in range(self.k):
            index = self.hash_functions[i].hash(x) % self.m
            if self.bit_array[index] == 0:
                return False
        return True

    def batch_insert(self, items):
        for item in items:
            self.insert(item)

# bf = BloomFilter(m=16, k=3, n=6)
# print(bf.bit_array)  # Prints the initial state of the bit array

# bf.insert(2)
# bf.insert(3)
# bf.insert(9)

# print(bf.bit_array)  # Prints the state of the bit array after inserting x

# print(bf.lookup(2))  
# print(bf.lookup(19))  

# items = [21, 7]  # List of n-bit numbers
# bf.batch_insert(items)
# print(bf.bit_array)  # Prints the state of the bit array after batch inserting items
# print(bf.lookup(22))  # Prints True if x is possibly in the set, False otherwise
# print(bf.lookup(7))  # Prints True if x is possibly in the set, False otherwise



# Generate 10000 64-bit numbers at random
S = [random.getrandbits(64) for _ in range(10000)]

results = []

for m in [2**i for i in range(6, 17)]:  # 64, 128, 256, ..., 65536
    for k in [1, 2, 4, 8, 16, int(math.log2(m//2))] :  # 1, 2, 4, ..., m/2 [2**i for i in range(int(math.log2(m//2)) + 1)]
        # Create a BF with params m=m, k=k, n=64
        bf = BloomFilter(m=m, k=k, n=64)
        
        for q in [m*(2**i) for i in range(7)]:  # m, 2m, 4m, ..., 64m
            # Generate q 64-bit numbers and batch insert them all into the BF
            bf.batch_insert([random.getrandbits(64) for _ in range(q)])
            
            # Generate 1000 random 64-bit numbers from scratch
            test_numbers = [random.getrandbits(64) for _ in range(1000)]
            
            # Calculate the proportion of these 1000 numbers on which the BF answers YES
            false_positive_rate = sum(bf.lookup(x) for x in test_numbers) / 1000
            
            # Store the results
            results.append((m, k, q, false_positive_rate))

# Convert the results to a DataFrame
df = pd.DataFrame(results, columns=['m', 'k', 'q', 'False Positive Rate'])

print(df)
