import re
from collections import Counter

class Autocorrect:
    def __init__(self, corpus: str):
        self.WORDS = Counter(re.findall(r'\w+', corpus.lower()))
        self.total = sum(self.WORDS.values())

    def probability(self, word: str) -> float:
        return self.WORDS[word] / self.total

    def correction(self, word: str) -> str:
        return max(self.candidates(word), key=self.probability)

    def candidates(self, word: str):
        return (self.known([word]) or
                self.known(self.edits1(word)) or
                [word])

    def known(self, words):
        return set(w for w in words if w in self.WORDS)

    def edits1(self, word: str):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word)+1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)
