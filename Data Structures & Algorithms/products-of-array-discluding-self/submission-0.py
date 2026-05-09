import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      res = []
      l =1
      r =1

      for i in range(len(nums)):
        l = nums[:i]
        r = nums[i+1:]
        res.append(math.prod(l)*math.prod(r))
     
      return res



        