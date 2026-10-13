class Solution:
    def confusingNumber(self, n: int) -> bool:
        invertMap = {"0":"0","1":"1","6":"9","9":"6","8":"8"}
        stringN = str(n)
        rotated = []
        for ch in reversed(stringN):
            if ch not in invertMap:
                return False
            rotated.append(invertMap[ch])
        return int("".join(rotated)) != n