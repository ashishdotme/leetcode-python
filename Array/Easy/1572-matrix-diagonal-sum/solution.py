# Created by Ashish Patel at 2025/01/09 14:45
# leetgo: 1.4.11
# https://leetcode.com/problems/matrix-diagonal-sum/

"""
1572. Matrix Diagonal Sum (Easy)
Given a square matrix `mat`, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the
secondary diagonal that are not part of the primary diagonal.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png)

```
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
```

**Example 2:**

```
Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
```

**Example 3:**

```
Input: mat = [[5]]
Output: 5
```

**Constraints:**

- `n == mat.length == mat[i].length`
- `1 <= n <= 100`
- `1 <= mat[i][j] <= 100`

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
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag1 = []
        for i in range(len(mat)):
            diag1.append(mat[i][i])

        diag2 = []
        for i in range(len(mat)):
            if i != abs(len(mat)-i-1):
                diag2.append(mat[i][abs(len(mat)-i-1)])

        return sum(diag1) + sum(diag2)
# @lc code=end

if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    ans = Solution().diagonalSum(mat)
    print("\noutput:", serialize(ans, "integer"))
