class Solution:
    def neighbours(self, i, j):
        neig = []

        if i < self.row - 1:
            neig.append((i + 1, j))
        if i > 0:
            neig.append((i - 1, j))
        if j < self.col - 1:
            neig.append((i, j + 1))
        if j > 0:
            neig.append((i, j - 1))

        return neig

    def searchFrom(self, i, j, word, path):
        if word == self.board[i][j]:
            return True

        path.add((i, j))

        found = False
        for n in self.neighbours(i, j):
            x, y = n
            if self.board[x][y] == word[1] and (x, y) not in path:
                found |= self.searchFrom(x, y, word[1:], path)
        
        return found

    def exist(self, board, word):
        self.row = len(board)
        self.col = len(board[0])
        self.board = board
        
        word = word[::-1]
        queue = []
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == word[0]:
                    queue.append((i, j))
                    
        res = []
        for valid in queue:
            i, j = valid
            res.append(self.searchFrom(i, j, word, set()))
        
        return any(res)