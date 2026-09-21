class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for index, val in enumerate(nums):
            if target - val in values:
                return[values[target-val],index]
            values[val] = index