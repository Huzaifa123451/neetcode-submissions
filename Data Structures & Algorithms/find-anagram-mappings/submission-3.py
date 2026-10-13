class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        valueToPos = {}
        res = [0] * len(nums1)
        for i in range(len(nums2)):
            valueToPos[nums2[i]] = i
        
        mapping = [0] * len(nums1)
        for i in range(len(nums1)):
            mapping[i] = valueToPos[nums1[i]]
        return mapping