class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = {}
        for i in s:
            res[i] = res.get(i,0) + 1
        for i in range(len(s)):
            if res[s[i]] == 1:
                return i

        return -1