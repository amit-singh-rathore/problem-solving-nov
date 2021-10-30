class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        m = max(len(words), max([len(word) for word in words]))
        w_pad = []
        for word in words:
            if len(word)!= m:
                word = word + (m-len(word))*'X'
                w_pad.append(word)
            else:
                w_pad.append(word)
                
        if len(w_pad)!= m:
            for i in range(m-len(w_pad)):
                w_pad.append('X'*m)
        
        for i in range(m):
            for j in range(m):
                if w_pad[i][j] != w_pad[j][i]:
                    return False
        return True

# No Extra space

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            if len(words) < len(words[i]):
                return False
            for j in range(len(words[i])):
                if len(words[j]) <= i:
                    return False
                if words[i][j] != words[j][i]:
                    return False
        return True