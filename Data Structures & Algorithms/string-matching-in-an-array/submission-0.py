class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        seen = set()
        result = []
        i = 0
        for i,w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if w1 != w2 and w1 in w2 and w1 not in seen:
                    seen.add(w1)
                    result.append(w1)
                    break
               
        return result
