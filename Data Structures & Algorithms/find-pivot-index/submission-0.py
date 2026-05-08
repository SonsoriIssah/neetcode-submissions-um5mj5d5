class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left =0
        right = sum(nums[1:])

        for i in range(len(nums)):
           
            if left == right:
                return i
            if i == len(nums) - 1:
                break
            else:
                left += nums[i]
                right -= nums[i+1]
        return -1