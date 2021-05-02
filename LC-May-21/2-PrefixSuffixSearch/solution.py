class WordFilter:

    def __init__(self, words: List[str]):
        self.wordmap = {}
        for idx, word in enumerate(words):
            for i in range(len(word)):
                for j in range(len(word)):
                    key = word[:i+1] + "#" + word[j:]
                    self.wordmap[key] = idx
            
        
        

    def f(self, prefix: str, suffix: str) -> int:
        lookupkey = prefix + "#" + suffix;
        return self.wordmap.get(lookupkey, -1)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)