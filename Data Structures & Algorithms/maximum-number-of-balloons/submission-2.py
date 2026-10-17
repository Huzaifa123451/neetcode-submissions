class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        minA_B = min(counts['a'],counts['b'])
        min_with_L = min(minA_B,counts['l'] // 2)
        return min(min_with_L,counts['o'] // 2)

        