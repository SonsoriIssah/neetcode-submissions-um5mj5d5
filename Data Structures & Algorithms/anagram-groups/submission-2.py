class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        val = defaultdict(list)


        for word in strs:
            indexs = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                indexs[index] += 1
            val[tuple(indexs)].append(word)
        return list(val.values())

            