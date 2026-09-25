class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = {}

        for i in s:
            char[i] = char.get(i,0) + 1
        
        for i, c in enumerate(s):
            if char[c] == 1:
                return i

        return -1
