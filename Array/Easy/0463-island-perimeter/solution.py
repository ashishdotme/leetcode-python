# Created by Ashish Patel at 2024/12/10 13:50
# leetgo: 1.4.11
# https://leetcode.com/problems/island-perimeter/

"""
463. Island Perimeter (Easy)
You are given `row x col` `grid` representing a map where `grid[i][j] = 1` represents land and
`grid[i][j] = 0` represents water.

Grid cells are connected **horizontally/vertically** (not diagonally). The `grid` is completely
surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the
island. One cell is a square with side length 1. The grid is rectangular, width and height don't
exceed 100. Determine the perimeter of the island.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/12/island.png)

```
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
```

**Example 2:**

```
Input: grid = [[1]]
Output: 4
```

**Example 3:**

```
Input: grid = [[1,0]]
Output: 4
```

**Constraints:**

- `row == grid.length`
- `col == grid[i].length`
- `1 <= row, col <= 100`
- `grid[i][j]` is `0` or `1`.
- There is exactly one island in `grid`.

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
import leetcode as lc
import numpy as np
# @lc code=begin

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        overlappingPerimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if(grid[row][col] == 0):
                    continue
                if(grid[row][col] == 1):
                    perimeter += 1
                    if(col < len(grid[row]) -1 ):
                        if(grid[row][col+1] == 1):
                            overlappingPerimeter += 1
                    if(row < len(grid) - 1):
                        if(grid[row+1][col] == 1):
                            overlappingPerimeter += 1
        return perimeter * 4 - overlappingPerimeter * 2
        

# @lc code=end

if __name__ == "__main__":
    #grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    ans = Solution().islandPerimeter(grid)
    print("\noutput:", serialize(ans, "integer"))
