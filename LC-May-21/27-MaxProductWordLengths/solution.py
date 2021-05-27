class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        
        words_set = []
        for word in words:
            words_set.append(set(word))
        
        for i in range(1, len(words)):
            for j in range(i):
                if not words_set[i].intersection(words_set[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans