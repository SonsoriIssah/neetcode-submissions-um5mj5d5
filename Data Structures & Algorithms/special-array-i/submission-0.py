class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def is_even(a):
            if a%2 == 0:
                return True
            else:
                return False
        L = 0
        R = 1
        for i in range(len(nums)-1):
            if is_even(nums[L]) == is_even(nums[R]):
                return False
            L+=1
            R+=1
        return True


        