class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0 
        freq = defaultdict(int)
        for i, x in enumerate(word): 
            if x in "aeiou": 
                if not i or word[i-1] not in "aeiou": 
                    jj = j = i # set anchor
                    freq.clear()
                freq[x] += 1
                while len(freq) == 5 and all(freq.values()): 
                    freq[word[j]] -= 1
                    j += 1
                ans += j - jj
        return ans 
        # return sum ( set(word[i:j])==set("aeiou") for i in range(0,len(word)-4) for j in range(i+5,len(word)+1) )
        # count = 0
        # for i in range(0, len(word) - 5 + 1):
        #     for j in range(i + 5, len(word) + 1):
        #         if set(word[i:j]) == set("aeiou"):
        #             count += 1
        # return count

        