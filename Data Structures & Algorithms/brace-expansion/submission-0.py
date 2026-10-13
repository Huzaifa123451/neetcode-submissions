class Solution:
    def expand(self, s: str) -> List[str]:
        i = 0
        options = []
        while i < len(s):
            if s[i] == "{":
                end = s.index("}", i)
                choices = s[i + 1:end].split(",")
                options.append(choices)
                i = end + 1
            else:
                options.append([s[i]])
                i += 1

        # ['{a,b}','c', '{d,e}',f]
        words = [""]

        for choices in options:
            words = [word + letter 
            for word in words
            for letter in choices]
        return sorted(words)