class Solution:


    def strStr(self, haystack: str, needle: str) -> int:

        def compute_prefix_function(P, m):
            pi = [0] * m
            k = 0
            for q in range(1, m):
                while k > 0 and P[k] != P[q]:
                    k = pi[k-1]
                if P[k] == P[q]:
                    k += 1
                pi[q] = k
            return pi

        def kmp_search(T, P, n, m):
            pi = compute_prefix_function(P, m)
            q = 0
            for i in range(n):
                while q > 0 and T[i] != P[q]:
                    q = pi[q - 1]

                if T[i] == P[q]:
                    q += 1

                if q == m:
                    return i - m + 1

            return -1
        return kmp_search(haystack, needle, len(haystack), len(needle))


        # m = len(haystack)
        # n = len(needle)
        # if m < n: return -1
        # if m == n: return 0 if haystack == needle else -1

        # for i in range(m - n + 1):
        #     substr = haystack[i:i+n]
        #     if substr == needle:
        #         return i
        # return -1
        