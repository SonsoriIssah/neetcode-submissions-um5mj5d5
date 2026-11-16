class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        i,res =0,[]

        while i< len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i= j+1
            j = length + i
            # 5#Hello
            """
            i = 0-s[5], j =0
            j= 1, length = 5, 
            i = 2[H], j = 6[o]
            
            """
            word = s[i:j]
            res.append(word)
            i=j
        
        return res


