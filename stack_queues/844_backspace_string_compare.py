class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        slst = []
        tlst = []

        for ch in s:
            if ch == '#':
                if slst:
                    slst.pop() 
                else:
                    continue
            else:
                slst.append(ch)
        for ch in t:
            if ch == '#':
                if tlst:
                    tlst.pop() 
                else:
                    continue
            else:
                tlst.append(ch)
        return slst == tlst