class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointL = 0
        pointR = len(numbers) - 1

        while numbers[pointL] + numbers[pointR] != target:
            if numbers[pointL] + numbers[pointR] > target:
                pointR -= 1
            elif numbers[pointL] + numbers[pointR] < target:
                pointL += 1

        return ([pointL+1,pointR+1])
        