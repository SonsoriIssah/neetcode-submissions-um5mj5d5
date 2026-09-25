class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            index = [0] *26
            for letter in i:
                val = ord(letter) - ord('a')
                index[val] += 1
            res[tuple(index)].append(i)
        return list(res.values())

