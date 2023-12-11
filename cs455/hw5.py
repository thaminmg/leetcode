import time

# Question 1

def compute_transition_function(pattern, m):
    alphabet = {'0', '1'}
    TF = [{} for _ in range(m+1)]
    for state in range(m + 1):
        for char in alphabet:
            next_state = 0 if state == m else state + 1
            while next_state > 0 and char != pattern[next_state - 1]:
                next_state = TF[next_state - 1].get(char, 0)
            TF[state][char] = next_state       
    return TF

def fsa_search(pattern, text):
    m = len(pattern)
    n = len(text)
    TF = compute_transition_function(pattern, m)
    matches = []
    state=0

    for i in range(n):
        state = TF[state].get(text[i], 0)
        if state == m:
            matches.append(i - m + 1)
            state = 0
    return matches

text = "00100100101001001"
pattern = "001"
print(fsa_search(pattern, text))

# Question 2
def compute_prefix_function(P, m):
    pi = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and P[q] != P[k]:
           k = pi[k - 1]

        if P[q] == P[k]:
            k += 1

        pi[q] = k

    return pi

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

text = "00100100101001001"
pattern = "001"
print(kmp_search(pattern, text))

def evaluate_build_time(algorithm, patterns):
    results = []
    for pattern in patterns:
        start_time = time.time()
        algorithm(pattern, len(pattern))
        end_time = time.time()
        elapsed_time = end_time - start_time
        results.append(elapsed_time)
    return results



# # Question 3
patterns_q3 = [
    ''.join(str(bit) for bit in [0, 1] * 5),
    ''.join(str(bit) for bit in [0, 1] * 50),
    ''.join(str(bit) for bit in [0, 1] * 500),
    ''.join(str(bit) for bit in [0, 1] * 5000),
    ''.join(str(bit) for bit in ([0, 1, 0] * 3) + [0, 0] * 4),
    ''.join(str(bit) for bit in ([0, 1, 0] * 3) + [0, 0] * 99),
    ''.join(str(bit) for bit in ([0, 1, 0] * 10) + [0, 0] * 99),
    ''.join(str(bit) for bit in ([0, 1, 0] * 10) + [0, 0] * 999),
]

results_q3_fsa_build = evaluate_build_time(compute_transition_function, patterns_q3)
results_q3_kmp_build = evaluate_build_time(compute_prefix_function, patterns_q3)

# Display results
print("Results for FSA Build Time:")
print("| Pattern Length  | 10     | 50    | 500   | 5000  | (010^3 0000)^10 | (010^3 0000)^100 | (010^10 0000)^100 | (010^10 0000)^1000 |")
print("|-----------------|--------|-------|-------|-------|-----------------|------------------|---------------------|----------------------|")
print(f"| Build Time      | {results_q3_fsa_build[0]:.4f} | {results_q3_fsa_build[1]:.4f} | {results_q3_fsa_build[2]:.4f} | {results_q3_fsa_build[3]:.4f} | {results_q3_fsa_build[4]:.4f}       | {results_q3_fsa_build[5]:.4f}         | {results_q3_fsa_build[6]:.4f}            | {results_q3_fsa_build[7]:.4f}             |")

print("\nResults for KMP Build Time:")
print("| Pattern Length  | 10     | 50    | 500   | 5000  | (010^3 0000)^10 | (010^3 0000)^100 | (010^10 0000)^100 | (010^10 0000)^1000 |")
print("|-----------------|--------|-------|-------|-------|-----------------|------------------|---------------------|----------------------|")
print(f"| Build Time      | {results_q3_kmp_build[0]:.4f} | {results_q3_kmp_build[1]:.4f} | {results_q3_kmp_build[2]:.4f} | {results_q3_kmp_build[3]:.4f} | {results_q3_kmp_build[4]:.4f}       | {results_q3_kmp_build[5]:.4f}         | {results_q3_kmp_build[6]:.4f}            | {results_q3_kmp_build[7]:.4f}             |")


# # Question 4

def evaluate_match_time(algorithm, text, patterns):
    results = []
    for pattern in patterns:
        # algorithm_data = algorithm(pattern, text)
        start_time = time.time()
        # algorithm_data(text, pattern)
        algorithm(pattern, text)
        end_time = time.time()
        elapsed_time = end_time - start_time
        results.append(elapsed_time)
    return results

patterns_q4 = ['01110011', '10000000']
n_values_q4 = [100, 1000]

results_q4_fsa_match = []
results_q4_kmp_match = []

for pattern in patterns_q4:
    for n in n_values_q4:
        text = ''.join(str(bit) for bit in [0, 1] * (n // 2))
        positions = [i for i in range(0, n, n // 20)][:5]
        
        for pos in positions:
            text = text[:pos] + pattern + text[pos + len(pattern):]
        
        result_fsa = evaluate_match_time(fsa_search, text, [pattern])
        result_kmp = evaluate_match_time(kmp_search, text, [pattern])
        
        results_q4_fsa_match.append(result_fsa[0])
        results_q4_kmp_match.append(result_kmp[0])


print("\nResults for FSA Match Time:")
print("| Pattern | Text Length | 100  | 1000 |")
print("|---------|-------------|------|------|")
print(f"| 01110011| Match Time  | {results_q4_fsa_match[0]:.4f} | {results_q4_fsa_match[1]:.4f} |")
print(f"| 10000000| Match Time  | {results_q4_fsa_match[2]:.4f} | {results_q4_fsa_match[3]:.4f} |")

print("\nResults for KMP Match Time:")
print("| Pattern | Text Length | 100  | 1000 |")
print("|---------|-------------|------|------|")
print(f"| 01110011| Match Time  | {results_q4_kmp_match[0]:.4f} | {results_q4_kmp_match[1]:.4f} |")
print(f"| 10000000| Match Time  | {results_q4_kmp_match[2]:.4f} | {results_q4_kmp_match[3]:.4f} |")
