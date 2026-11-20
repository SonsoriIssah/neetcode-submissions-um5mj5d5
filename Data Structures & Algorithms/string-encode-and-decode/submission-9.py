class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedWord = ''
        for i in strs:
            encodedWord += str(len(i)) + '#' + i
        return encodedWord

    def decode(self, s: str) -> List[str]:
        l,decodedWord = 0,[]

        while l< len(s):
            r = l
            while s[r] != '#':
                r += 1
            length = int(s[l:r]) # 5#Hello
            
            decodedWord.append(s[r+1:r+1+length])
            l =r+1+length
        
        return decodedWord

        

