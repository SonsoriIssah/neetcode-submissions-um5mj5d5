class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for i in s:
            count_s[i] = s.count(i)
        for i in t:
            count_t[i] = t.count(i)
        for i in count_s:
            if i not in count_t:
                return False
            else:
                if count_s[i] !=  count_t[i]:
                    return False
        return True