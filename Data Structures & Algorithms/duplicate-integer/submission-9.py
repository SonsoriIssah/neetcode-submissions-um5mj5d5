class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Input: Array of numbers
        Output: Bool(True/False)

        we are given an arrayf of number , we should find out if there are any duplicate numbers and return true if so else False

        1.Is there a case where the array can be empty and if it can be empty what do we retun
        2.Can multiple values repeat
        
        [1,2,3,3] ->  [3,3], True
        [] ->
        [1,2,3,4] -> False

        Plan:
        1.Store the numbers in a set
        2. compare the size of the set to the size of the array
        """
        values = set([i for i in nums ])
        return len(values) < len(nums)
        


        