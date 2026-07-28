class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = 1
        diff = {}
        for i in range(len(nums)):
            if nums[i] in diff:
                return [diff[nums[i]], i]
            diff[target - nums[i]] = i
        return [0,1]
        