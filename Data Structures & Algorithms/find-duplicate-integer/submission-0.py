class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       seen = defaultdict()
       for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
            if seen[num] != 1:
                return num
        