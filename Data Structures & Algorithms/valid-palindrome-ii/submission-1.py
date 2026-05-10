class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # Try skipping either the left or right character
                return isPalin(l + 1, r) or isPalin(l, r - 1)
            l, r = l + 1, r - 1

        return True
                
        