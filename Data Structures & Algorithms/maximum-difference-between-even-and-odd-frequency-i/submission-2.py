class Solution:
    def maxDifference(self, s: str) -> int:

        charFrequencies = defaultdict(int)
        max_diff = -10000000
        for char in s:
            if char in charFrequencies:
                charFrequencies[char] += 1
            else:
                charFrequencies[char] = 1

        odd_freqs = [freq for freq in charFrequencies.values() if freq % 2 != 0]
        even_freqs = [freq for freq in charFrequencies.values() if freq % 2 == 0]

        return max(odd_freqs) - min(even_freqs)