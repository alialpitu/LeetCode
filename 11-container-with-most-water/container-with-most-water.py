class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0

        while l < r:
            result = max(result,(r-l)*min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                while height[l] == height[r] and l < r:
                    l += 1

        return result
        