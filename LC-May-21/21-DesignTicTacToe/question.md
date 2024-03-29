## Design Tic-Tac-Toe

Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

- A move is guaranteed to be valid and is placed on an empty block.
- Once a winning condition is reached, no more moves are allowed.
- A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the TicTacToe class:

- TicTacToe(int n) Initializes the object the size of the board n.
- int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.

## Example:
```
Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]
```

## Constraints

- 2 <= n <= 100
- player is 1 or 2.
- 0 <= row, col < n
- (row, col) are unique for each different call to move.
- At most n2 calls will be made to move.