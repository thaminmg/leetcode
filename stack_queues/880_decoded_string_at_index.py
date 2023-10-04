class Solution:
    def decodeAtIndex(self, encodedString: str, k: int) -> str:
        character_lengths = [0]
        for i in range(len(encodedString)):
            if encodedString[i].isdigit():
                length = character_lengths[-1] * int(encodedString[i])
                character_lengths.append(length)
            else:
                length = character_lengths[-1] + 1
                character_lengths.append(length)

        ln = len(character_lengths)
        while character_lengths:
            k %= character_lengths[-1]
            ln -= 1
            if k == 0 and encodedString[ln - 1].isalpha():
                return encodedString[ln - 1]
            character_lengths.pop()

        return "" 

# class Solution:
#     def decodeAtIndex(self, s: str, k: int) -> str:
#         res = []
#         counter = 1
#         for c in s:
#             if '0' <= c <= '9':
#                 integer = int(c)
#                 string = ''.join(res)
#                 res = list(string * (integer))
#             else:
#                 res.append(c)
#             if len(res) >= k:
#                 return res[k-1]
#             counter += 1
#         return ''