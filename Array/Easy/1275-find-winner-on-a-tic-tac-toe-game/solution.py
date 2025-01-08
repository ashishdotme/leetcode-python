# Created by Ashish Patel at 2025/01/07 19:57
# leetgo: 1.4.13
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

"""
1275. Find Winner on a Tic Tac Toe Game (Easy)
**Tic-tac-toe** is played by two players `A` and `B` on a `3 x 3` grid. The rules of Tic-Tac-Toe are:

- Players take turns placing characters into empty squares `' '`.
- The first player `A` always places `'X'` characters, while the second player `B` always places
`'O'` characters.
- `'X'` and `'O'` characters are always placed into empty squares, never on filled ones.
- The game ends when there are **three** of the same (non-empty) character filling any row, column, or
diagonal.
- The game also ends if all squares are non-empty.
- No more moves can be played if the game is over.

Given a 2D integer array `moves` where `moves[i] = [rowᵢ, colᵢ]` indicates that the `iᵗʰ` move will
be played on `grid[rowᵢ][colᵢ]`. return the winner of the game if it exists ( `A` or `B`). In case
the game ends in a draw return `"Draw"`. If there are still movements to play return `"Pending"`.

You can assume that `moves` is valid (i.e., it follows the rules of **Tic-Tac-Toe**), the grid is
initially empty, and `A` will play first.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/09/22/xo1-grid.jpg)

```
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/09/22/xo2-grid.jpg)

```
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2021/09/22/xo3-grid.jpg)

```
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
```

**Constraints:**

- `1 <= moves.length <= 9`
- `moves[i].length == 2`
- `0 <= rowᵢ, colᵢ <= 2`
- There are no repeated elements on `moves`.
- `moves` follow the rules of tic tac toe.

"""

from typing import *
from leetgo_py import *

import bisect
import collections 
import functools
import heapq 
import itertools 
import operator
import math 
import string
import numpy as np
# @lc code=begin

class Solution:
    def board_state(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
                return 'A' if board[i][0] == 'X' else 'B'
        
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
                return 'A' if board[0][i] == 'X' else 'B'
        
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
            return 'A' if board[0][0] == 'X' else 'B'
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
            return 'A' if board[0][2] == 'X' else 'B'
        
        return None
                
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [["" for _ in range(3)] for _ in range(3)]
        for idx, move in enumerate(moves):
            row, col = move
            matrix[row][col] = 'X' if idx % 2 == 0 else 'O'
        board = self.board_state(matrix)
        if board:
            return board
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

                
# @lc code=end

if __name__ == "__main__":
    moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    ans = Solution().tictactoe(moves)
    print("\noutput:", serialize(ans, "string"))
