class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        sim = set((u, v) for u, v in similarPairs) | set((v, u) for u, v in similarPairs)
        return all(word1 == word2 or (word1, word2) in sim for word1, word2 in zip(sentence1, sentence2))