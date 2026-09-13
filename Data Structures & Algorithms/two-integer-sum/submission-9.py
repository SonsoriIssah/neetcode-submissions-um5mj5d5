class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for index, value in enumerate(nums):
            if target - value in res:
                return [res[target-value],index]
            res[value] = index
        