class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums)):
            multiplier = 1
            for j in range(len(nums)):
                if i != j: 
                    multiplier = multiplier * nums[j]
            result.append(multiplier)

        return result