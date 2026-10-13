class Solution:
    def expand(self, s: str) -> List[str]:
        i = 0
        options = []
        while i < len(s):
            if s[i] == "{":
                end = s.index("}", i)
                choices = s[i + 1:end].split(",") # {a,b} becomes ["a","b"]
                options.append(choices)
                i = end + 1
            else:
                options.append([s[i]])
                i += 1

        # options = [["a","b"], ["c"], ["d","e"],["f"]]
        words = [""]

        for choices in options:
            new_words = []
            for word in words:
                for letter in choices:
                    new_words.append(word + letter)

            words = new_words

        return sorted(words)
        