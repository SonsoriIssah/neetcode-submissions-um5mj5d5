class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i,v in enumerate(nums):
            diff = target - v
            if diff in result:
                return [result[diff],i]
            else:
                result[v] = i