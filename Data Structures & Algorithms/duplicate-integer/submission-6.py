class Solution:
        def hasDuplicate(self, nums: List[int]) -> bool:
            values = {}
            for index,val  in enumerate(nums):
                if val not in values:
                    values[val] = index
                else:
                    return True
            return False