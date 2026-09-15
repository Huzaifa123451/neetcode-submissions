class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        isAnagram = {}
        lst = []
        if strs == [""]:
            return [[""]]
        elif len(strs) == 1:
            return [strs]
        else:
            res = defaultdict(list)
            for s in strs:
                count = [0] * 26
                for c in s:
                   count[ord(c) - ord('a')] += 1
                res[tuple(count)].append(s)
            return list(res.values())
            