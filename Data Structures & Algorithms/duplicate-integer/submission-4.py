class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        index = 0

        for i in nums:
            if i in values:
               

                return True
            else:
                values[i] = index
                index += 1
        

        return False
        