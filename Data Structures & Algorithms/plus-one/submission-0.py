class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strNum = ""
        num = 0
        for digit in digits:
            strNum += str(digit)
        num = int(strNum) + 1
        res = []
        for c in str(num):
            res.append(c)
        return res