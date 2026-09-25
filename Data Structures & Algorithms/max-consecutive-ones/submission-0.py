class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max1 = 0
        lp = 0
        if not nums:
            return 0
        for num in nums:
            if num == 1:
                lp += 1
                max1 = max(max1, lp)
            else:
                lp = 0
        return max1