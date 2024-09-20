class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            print(nums[l:r+1])
            m = (l+r)//2
            if nums[m] == target:
                return(m)
            # soldaki kume
            if nums[m] >= nums[r]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            #sagdaki kume
            elif nums[m] <= nums[r]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            
        return(-1)