class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for i in nums:
            if vals.get(i):
                return True
            vals[i] = True 
        return False