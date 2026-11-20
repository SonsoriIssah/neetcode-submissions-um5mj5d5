class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        leftProd = 1

        for i in range(len(nums)):
            res[i] *= leftProd
            leftProd *= nums[i]
            

        # [1,1,2,8] 
        rightProd = 1  

        for i in range(len(nums)-1,-1,-1):
            res[i] *= rightProd
            rightProd *= nums[i] 
        
        return res
        