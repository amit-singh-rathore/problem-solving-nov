def isValidSudoku(board):
    row_map = { i:set() for i in range(0, 9)}
    col_map =  { i:set() for i in range(0, 9)}
    box_map = { j//3 + (i//3)*3 : set() for i in range(0, 9) for j in range(0,9)}
        
    for row in range(9):
        for col in range(9):
            cur_char = board[row][col]
            if cur_char != '.':
                if cur_char in row_map[row]:
                    return False
                else:
                    row_map[row].add(cur_char)
                    
                if cur_char in col_map[col]:
                    return False
                else:
                    col_map[col].add(cur_char)
                
                box = col//3 + (row//3)*3

                if cur_char in box_map[box]:
                    return False
                else:
                    box_map[box].add(cur_char)
            
    return True