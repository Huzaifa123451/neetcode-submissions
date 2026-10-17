class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        notAppeared = []        
        numRange = len(nums)
        numSet = set(nums)
        for i in range(1, numRange + 1):
            if i not in numSet:
                notAppeared.append(i)
        return notAppeared