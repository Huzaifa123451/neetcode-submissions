class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numAppearences = defaultdict(int)
        if not nums:
            return 0

        for num in nums:
            if num in numAppearences:
                numAppearences[num] += 1
            else:
                numAppearences[num] = 1

        for num, count in numAppearences.items():
            if count > len(nums) // 2:
                return num
        return 0