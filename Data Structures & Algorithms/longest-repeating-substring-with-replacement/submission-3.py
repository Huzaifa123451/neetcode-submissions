class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        maxf = 0
        lp = 0
        for rp in range(len(s)):
            count[s[rp]] = 1 + count.get(s[rp],0) 
            maxf = max(maxf,count[s[rp]])
            while (rp - lp + 1) - maxf  > k:
                count[s[lp]] -= 1
                lp += 1
            res = max(res, rp - lp + 1)
        return res