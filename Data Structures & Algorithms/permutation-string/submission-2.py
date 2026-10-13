class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_sorted = "".join(sorted(s1))
        
        l = 0
        r = len(s1) - 1

        while s1_sorted != "".join(sorted(s2[l:r+1])) and r < (len(s2) - 1):
            l += 1
            r += 1
        
        return s1_sorted == "".join(sorted(s2[l:r+1]))
