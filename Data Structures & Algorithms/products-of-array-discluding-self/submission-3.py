class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        preProd = 1
        for i in range(len(nums)):
            res[i] *= preProd
            preProd*= nums[i]
        

        postProd = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postProd
            postProd *= nums[i]
        return res

        
        

