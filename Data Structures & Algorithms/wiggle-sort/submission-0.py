class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        l = 0
        r = len(nums)-1
        while l != r:
            if nums[l] <= nums[r]:
                nums[l] = nums[r]
                l += 1
            elif nums[l] >= nums[r]:
                nums[r] = nums[l]
                r -= 1
        return nums