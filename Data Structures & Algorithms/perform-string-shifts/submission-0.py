class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s_copy = ""
        for i in range(0,len(shift)):
            amount_to_shift = shift[i][1]
            while amount_to_shift != 0:
                if shift[i][0] == 0: # left shift
                    s = s[1:] + s[0]
                elif shift[i][0] == 1: #right shift
                    last_character = s[-1]
                    s = s[0:-1]
                    s  = last_character + s
                amount_to_shift -= 1
        return s