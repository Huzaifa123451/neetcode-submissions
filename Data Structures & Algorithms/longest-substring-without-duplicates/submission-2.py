class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        if len(s) < 1:
            return 0
        else:
           for i in range(0,len(s)):
                newStr = set()
                for j in range(i,len(s)):
                    if s[j] in newStr:
                        break
                    newStr.add(s[j])
                count = max(count,len(newStr))
        return max(count,len(newStr))

            