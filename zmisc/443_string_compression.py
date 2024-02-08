class Solution:
    def compress(self, chars: list[str]) -> int:
        length = len(chars)
        count = 1
        lst = []
        after = ''
        prev = ''
        for i in range(length):
            if i == length - 1:
                after  = ''
            else:
                after = chars[i + 1]

            if chars[i] == after:
                count += 1
            else:
                if count == 1: 
                    lst.append(str(chars[i]))
                else:
                    lst.append(prev)
                    if count < 10:
                        lst.append(str(count))
                    else:
                        llst = []
                        while count:
                            remainder = count % 10
                            count = count // 10
                            llst.append(str(remainder))
                        for j in reversed(llst):
                            lst.append(j)
                    count = 1
            prev = chars[i]
        print(lst)


chars = ["a","a","b","b","c","c","c"]
print(Solution().compress(chars))