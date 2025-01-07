# Created by Ashish Patel at 2025/01/06 12:30
# leetgo: 1.4.13
# https://leetcode.com/problems/projection-area-of-3d-shapes/

"""
883. Projection Area of 3D Shapes (Easy)
You are given an `n x n` `grid` where we place some `1 x 1 x 1` cubes that are axis-aligned with the
`x`, `y`, and `z` axes.

Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of the cell `(i, j)`.

We view the projection of these cubes onto the `xy`, `yz`, and `zx` planes.

A **projection** is like a shadow, that maps our **3-dimensional** figure to a **2-dimensional**
plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png)

```
Input: grid = [[1,2],[3,4]]
Output: 17
Explanation: Here are the three projections ("shadows") of the shape made with each axis-aligned
plane.
```

**Example 2:**

```
Input: grid = [[2]]
Output: 5
```

**Example 3:**

```
Input: grid = [[1,0],[0,2]]
Output: 8
```

**Constraints:**

- `n == grid.length == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] <= 50`

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

# @lc code=begin

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(value > 0 for row in grid for value in row)
        yx = sum(max(row) for row in grid)
        xz = sum(max(col) for col in zip(*grid))
        return  xy + yx + xz

# @lc code=end

if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ans = Solution().projectionArea(grid)
    print("\noutput:", serialize(ans, "integer"))
