class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = ""
        seen = set()
        for num in nums:
            if num not in seen:
               seen.add(num)
            else:
                duplicate = num
                
        if duplicate in seen:
            return True
        return False
