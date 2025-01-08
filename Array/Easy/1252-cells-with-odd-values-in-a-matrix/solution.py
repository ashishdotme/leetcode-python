# Created by Ashish Patel at 2025/01/07 23:37
# leetgo: 1.4.13
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

"""
1252. Cells with Odd Values in a Matrix (Easy)
There is an `m x n` matrix that is initialized to all `0`'s. There is also a 2D array `indices`
where each `indices[i] = [rᵢ, cᵢ]` represents a **0-indexed location** to perform some increment
operations on the matrix.

For each location `indices[i]`, do **both** of the following:

1. Increment **all** the cells on row `rᵢ`.
2. Increment **all** the cells on column `cᵢ`.

Given `m`, `n`, and `indices`, return the **number of odd-valued cells** in the matrix after applying
the increment to all locations in  `indices`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/10/30/e1.png)

```
Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/10/30/e2.png)

```
Input: m = 2, n = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.
```

**Constraints:**

- `1 <= m, n <= 50`
- `1 <= indices.length <= 100`
- `0 <= rᵢ < m`
- `0 <= cᵢ < n`

**Follow up:** Could you solve this in `O(n + m + indices.length)` time with only `O(n + m)` extra
space?

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
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for indice in indices:
            row, col = indice
            for i in range(n):
                matrix[row][i] += 1
            for j in range(m):
                matrix[j][col] += 1
        odd_count = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] % 2 != 0:
                    odd_count += 1  
                  
        return odd_count
# @lc code=end

if __name__ == "__main__":
    m = 2
    n = 3
    indices = [[0,1],[1,1]]
    ans = Solution().oddCells(m, n, indices)
    print("\noutput:", serialize(ans, "integer"))
