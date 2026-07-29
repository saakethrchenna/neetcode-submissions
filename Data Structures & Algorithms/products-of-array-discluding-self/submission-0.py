class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = nums.copy()
        backward = nums.copy()
        out = nums.copy()
        for i in range(1,len(nums)):
            forward[i] *= forward[i-1]
        for i in range(len(nums)-2, -1, -1):
            backward[i] *= backward[i+1]

        for i in range(1,len(nums)-1):
            out[i] = forward[i-1] * backward[i+1]
        if len(nums) > 1:
            out[0] = backward[1]
            out[-1] = forward[-2]
        print(forward)
        print(backward)
        return out
        
        