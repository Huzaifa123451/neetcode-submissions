class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        first = 1
        last = max(piles)
        while first <= last:
            middle = ((first+last) // 2)
            total_time = sum(math.ceil(p/ middle) for p in piles)
            if total_time <= h:
                k = middle
                last = middle - 1
            else: 
                first = middle + 1
            
        return k