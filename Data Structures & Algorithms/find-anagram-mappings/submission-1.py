class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        res = [0] * len(nums1)

        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums2[j] == nums1[i]:
                    res[i] = j
        return res