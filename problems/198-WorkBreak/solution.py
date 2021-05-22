class Solution:
    def wordBreak(self, s: str, WordDict: List[str]) -> bool:
        q = deque()
        seen = set()
        for word in WordDict:
            if word == s:
                return True
            seen.add(word)
            if word == s[:len(word)]:
                q.append((word,len(word)))
        i=0
        
        while q:
            w, i = q.popleft()
            
            for word in WordDict:
                if i > len(s):
                    break
                if w+word == s:
                    return True
                elif w+word not in seen and w+word == s[:len(w+word)]:
                    q.append((w+word,len(w+word)))
                    seen.add(w+word)
        return False