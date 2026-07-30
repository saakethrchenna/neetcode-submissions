class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        maxv = 0
        for i in vals:
            for i in vals:
                if i-1 not in vals:
                    curr = i
                    lenv = 0
                    while curr in vals:
                        curr += 1
                        lenv += 1
                    maxv = max(lenv, maxv)
        return maxv
            

        