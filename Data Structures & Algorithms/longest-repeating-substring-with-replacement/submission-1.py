class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        seen = set(s)
        for char in seen:
            count = lp = 0
            for i in range(len(s)):
                if s[i] == char:
                    count += 1


                while (i - lp + 1) - count > k:
                    if s[lp] == char:
                        count -= 1
                    lp += 1

                res = max(res,i-lp+1)
        return res
        