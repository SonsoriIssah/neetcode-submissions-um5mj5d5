class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for index, val in enumerate(nums):
            if target- val in indices:
                return [indices[target-val],index]
            indices[val] = index