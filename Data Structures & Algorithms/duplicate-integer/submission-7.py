class Solution:
        def hasDuplicate(self, nums: List[int]) -> bool:
            values = set()
            for val  in nums:
                if val not in values:
                  values.add(val)
                else:
                    return True
            return False