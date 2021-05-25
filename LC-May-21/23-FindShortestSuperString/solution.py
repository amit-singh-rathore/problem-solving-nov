class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        if len(words)==1:
            return words[0]
        words.sort(key=lambda s: len(s))
        res = [words[0]]
        
        return self.shortest(words, res)
    
    
    def shortest(self, words, res):
        
        if len(words)==0:
            return res
        
        if not words[0] in res:
            return min(self.shortest(words[1:], res + [words[0]]), \
                       self.shortest(words[1:], [words[0]] + res), key = lambda x: len(x))
        else:
            return self.shortest(words[1:], res)