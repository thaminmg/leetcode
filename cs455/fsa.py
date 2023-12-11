class FSA:
    def __init__(self, pattern):
        self.pattern = pattern
        self.transition_table = self.build_transition_table()

    def build_transition_table(self):
        m = len(self.pattern)
        alphabet = {'0', '1'}
        transition_table = [{} for _ in range(m + 1)]

        for state in range(m + 1):
            for char in alphabet:
                next_state = 0 if state == m else state + 1
                while next_state > 0 and char != self.pattern[next_state - 1]:
                    next_state = transition_table[next_state - 1].get(char, 0)
                transition_table[state][char] = next_state

        return transition_table

    def find_matches(self, text):
        matches = []
        n = len(text)
        state = 0

        for i in range(n):
            state = self.transition_table[state].get(text[i], 0)

            if state == len(self.pattern):
                # Match found at index i - m + 1
                matches.append(i - len(self.pattern) + 1)
                state = 0  # Reset state to handle overlapping patterns

        return matches

def main():
    text = "00100100101001001"
    pattern = "001"
    fsa = FSA(pattern)
    matches = fsa.find_matches(text)

    print("Pattern found at indices:", matches)

if __name__ == "__main__":
    main()