class Solution:
    def largestGoodInteger(self, num: str) -> str:
        returnString = ""
        for i in range(2,len(num)):
            if num[i-2] == num[i-1] == num[i]:
                candidate = num[i-2:i+1]
                if candidate > returnString:
                    returnString = candidate
        return returnString