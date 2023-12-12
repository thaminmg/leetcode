import random
import time

# Question 1
def fsa_search(pattern, text):
    state = 0
    matches = []
    fsa = compute_transition_function(pattern, len(pattern))
    for i in range(len(text)):
        state = fsa[state][text[i]]
        if state == len(pattern):
            matches.append(i - len(pattern) + 1)
    return matches

def compute_transition_function(pattern, m):
    fsa = [{'0': 0, '1': 0} for _ in range(m + 1)]
    for q in range(m+1):
        for a in ['0', '1']:
            k = min(m, q+1)
            while k > 0 and pattern[:k] != pattern[q - k + 1:q] + a:
                k = k - 1
            fsa[q][a] = k
    return fsa

text = "011100111100111001101101110011"
pattern = "01110011"

print(fsa_search(pattern, text))

# Question 2
def kmp_search(pattern, text):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern, m)
    q = 0
    matches = []
    for i in range(n):
        while q > 0 and text[i] != pattern[q]:
            q = pi[q - 1]
        if text[i] == pattern[q]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = pi[q - 1]
    return matches

def compute_prefix_function(pattern, m):
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[q] != pattern[k]:
           k = pi[k - 1]
        if pattern[q] == pattern[k]:
            k += 1
        pi[q] = k
    return pi

text = "011100111100111001101101110011"
pattern = "01110011"
print(kmp_search(pattern, text))

# Question 3
def evaluate_build_time(algorithm, patterns):
    results = []
    for pattern in patterns:
        start_time = time.time()
        algorithm(pattern, len(pattern))
        end_time = time.time()
        elapsed_time = end_time - start_time
        results.append(elapsed_time)
    return results

def generate_random_pattern(length):
    return ''.join(random.choice(['0', '1']) for _ in range(length))

pattern_lengths = [10, 100, 1000] #10000
patterns = [generate_random_pattern(length) for length in pattern_lengths]
q32 = [
    ''.join(str(bit) for bit in ([0, 1, 0] * 3) + [0, 0, 0, 0]) * 10,
    ''.join(str(bit) for bit in ([0, 1, 0] * 3) + [0, 0, 0, 0]) * 100,
    ''.join(str(bit) for bit in ([0, 1, 0] * 10) + [0, 0, 0, 0]) * 100,
    ''.join(str(bit) for bit in ([0, 1, 0] * 10) + [0, 0, 0, 0]) * 1000
    ]
patterns.extend(q32)

results_fsa_build = evaluate_build_time(compute_transition_function, patterns)
results_kmp_build = evaluate_build_time(compute_prefix_function, patterns)

# Display results
print("Results for Build Time:")
print("|----------------------------------------------------------------|")
print("|   Pattern Length   |  FSA Build Time (s)  | KMP Build Time (s) |")
print("|--------------------|----------------------|--------------------|")
print(f"| 10                 |     {results_fsa_build[0]:.10f}     |    {results_kmp_build[0]:.10f}    |")
print(f"| 100                |     {results_fsa_build[1]:.10f}     |    {results_kmp_build[1]:.10f}    |")
print(f"| 1000               |     {results_fsa_build[2]:.10f}     |    {results_kmp_build[2]:.10f}    |")
# print(f"| 10000              |    {results_fsa_build[3]:.10f}    |    {results_kmp_build[3]:.10f}    |")
print(f"| (010^3 0000)^10    |     {results_fsa_build[3]:.10f}     |    {results_kmp_build[3]:.10f}    |")
print(f"| (010^3 0000)^100   |     {results_fsa_build[4]:.10f}     |    {results_kmp_build[4]:.10f}    |")
print(f"| (010^10 0000)^100  |     {results_fsa_build[5]:.10f}     |    {results_kmp_build[5]:.10f}    |")
print(f"| (010^10 0000)^1000 |    {results_fsa_build[6]:.10f}    |    {results_kmp_build[6]:.10f}    |")
print("|----------------------------------------------------------------|")
print()

# Question 4
def evaluate_match_time(algorithm, pattern, text):
    start_time = time.time()
    algorithm(pattern, text)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return  elapsed_time

patterns_q4 = ['01110011', '10000000']
values = [100, 1000]

results_fsa_match = []
results_kmp_match = []

for pattern in patterns_q4:
    for n in values:
        text = generate_random_pattern(n)
        positions = [random.randint(0, n) for _ in range(5)]
        
        for pos in positions:
            text = text[:pos] + pattern + text[pos + len(pattern):]
        
        result_fsa = evaluate_match_time(fsa_search, pattern, text)
        result_kmp = evaluate_match_time(kmp_search, pattern, text)
        
        results_fsa_match.append(result_fsa)
        results_kmp_match.append(result_kmp)

print("Results for Match Time:")
print("|--------------------------------------------------------------------------------------------------------|")
print("|                    | FSA Match Time (s)                      | KMP Match Time (s)                      |")
print("|--------------------|--------------------|--------------------|--------------------|--------------------|")
print("|   Pattern Length   | 100                | 1000               | 100                | 1000               |")
print("|--------------------|--------------------|--------------------|--------------------|--------------------|")
print(f"| 01110011           |    {results_fsa_match[0]:.10f}    |    {results_fsa_match[1]:.10f}    |    {results_kmp_match[0]:.10f}    |    {results_kmp_match[1]:.10f}    |")
print(f"| 10000000           |    {results_fsa_match[2]:.10f}    |    {results_fsa_match[3]:.10f}    |    {results_kmp_match[2]:.10f}    |    {results_kmp_match[3]:.10f}    |")
print("|--------------------------------------------------------------------------------------------------------|")
print()
