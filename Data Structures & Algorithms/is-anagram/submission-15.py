class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        charS = {}
        charT = {}

        for i in s:
            charS[i] = charS.get(i,0) + 1
        
        for i in t:
            charT[i] = charT.get(i,0) + 1
        
        return charT == charS

        

        