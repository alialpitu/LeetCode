class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            point1 = i + 1
            point2 = len(nums) - 1
            while point1 < point2:
                if nums[point1] + nums[point2] < -1*nums[i]:
                    point1 += 1
                elif nums[point1] + nums[point2] > -1 * nums[i]:
                    point2 -= 1
                elif nums[point1] + nums[point2] == -1*nums[i]:
                    result.append([nums[point1],nums[point2],nums[i]])
                    point1 += 1
                    while nums[point1] == nums[point1-1] and point1<point2:
                        point1 += 1

        return (result)
        