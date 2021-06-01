class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i, row in enumerate(board):
            box_i = (i//3)*3
            for j, char in enumerate(row):
                if char != ".":
                    if ("row", i, char) in seen:
                        return False
                    else:
                        seen.add(("row", i, char))
                    if ("col", j, char) in seen:
                        return False
                    else:
                        seen.add(("col", j, char))
                    box = j//3 + box_i
                    if ("box", box, char) in seen:
                        return False
                    else:
                        seen.add(("box", box, char))

        return True