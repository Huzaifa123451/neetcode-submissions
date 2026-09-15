class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArr = []
        for num in nums:
            newArr.append(num)
        return nums + newArr