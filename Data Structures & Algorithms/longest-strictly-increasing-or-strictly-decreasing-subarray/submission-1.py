class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest_increasing_so_far = 1
        longest_decreasing_so_far = 1
        lenCurrSubarray = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                lenCurrSubarray += 1
            else:
                lenCurrSubarray = 1
            longest_increasing_so_far = max(longest_increasing_so_far, lenCurrSubarray)
        lenCurrSubarray = 1
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                lenCurrSubarray += 1
            else:
                lenCurrSubarray = 1
            longest_decreasing_so_far = max(longest_decreasing_so_far, lenCurrSubarray)

        return max(longest_decreasing_so_far, longest_increasing_so_far)
