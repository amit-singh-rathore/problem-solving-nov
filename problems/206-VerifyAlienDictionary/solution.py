class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_order = {char : idx for idx, char in enumerate(order)}
        l = len(words)
        
        for i in range(1,l):
            prev = words[i-1]
            cur = words[i]
            
            for idx in range(len(prev)):
                if idx == len(cur):
                    return False
                if prev[idx] != cur[idx]:
                    if char_order[prev[idx]] > char_order[cur[idx]]:
                        return False
                    break
        return True