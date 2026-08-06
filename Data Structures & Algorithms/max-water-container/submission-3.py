class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxv = min(heights[end],heights[start]) * (end - start)
        while start < end:
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1 
            maxv = max(maxv, min(heights[end],heights[start]) * (end - start))
        return maxv