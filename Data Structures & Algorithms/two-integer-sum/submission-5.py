class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input:Array
        Output: Array of indices

        Restatement:  Find two numbers int he array that sum up to a given target and return theur indices
        1. Wha

        Plan:
        1. Create a hashmap to store values and their indexes
        2. Loop over the array and subtract values from the target and store that difference in the hashmap
        3. Check if the values is present in the hashmap 
        4. Return indices
        Test Cases:
        [3,4,5,6] , 7
        {4:0,}

        """
        val = {}

        for index,value in enumerate(nums):
            difference = target - value
            if value in val:
                return[val[value],index]
            else:
                val[difference] = index
       

        