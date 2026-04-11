class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = {}
        if nums == None:
         return []

        for i, val in enumerate(nums):
            difference = target - val
            if difference in indexs:
                return [indexs[difference], i]
                
            else:
             indexs[val] = i
        return []