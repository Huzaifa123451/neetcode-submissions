class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
      numCount = defaultdict(int)
      res = []
      for num in nums:
        if num in numCount:
            numCount[num] += 1
        else:
            numCount[num] = 1

      for num in numCount:
        if numCount[num] == 1:
            res.append(num)
        
      return max(res) if res else -1