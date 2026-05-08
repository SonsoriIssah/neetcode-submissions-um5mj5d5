class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for index,value in enumerate(nums):
            diff = target - value
            if diff in val:
                return [val[diff],index]
            else:
                val[value] = index