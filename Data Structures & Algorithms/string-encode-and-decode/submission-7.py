class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        i,res = 0,[]

        while i< len(s):
            j = i
            #4#abc
            while s[j] != '#':
                j+=1
            
            length = int(s[i:j])
            i =j+1
            j= length +i
            word = s[i:j]
            res.append(word)
            i = j 
        return res
