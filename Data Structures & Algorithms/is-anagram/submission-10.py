class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Input: String
        Output: Bool

        We should return True if two strings have the same characters in the word irrespective of arrangement, else False

        1. Can the string be empty
        
        Plan:
        1. We could sort each of the words using sort()
        2. compare each values , and return that output

        1.Create a hashmap and store the number of occurrence of each values
        2. compare the 2 hashmaps
        """

        word_s = {}
        word_t = {}

        for i in s:
            word_s[i] = word_s.get(i,0) + 1
        for i in t:
            word_t[i] = word_t.get(i,0) + 1
        return word_s == word_t


        