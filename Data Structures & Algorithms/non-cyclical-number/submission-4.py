class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        answer = n
        while answer != 1:
            if answer in seen:
                return False               
            else:
                seen.add(answer)
                temp = 0
                for char in str(answer):
                    temp += (int(char) * int(char))
                answer = temp    
        return True
        
