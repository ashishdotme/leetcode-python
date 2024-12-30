# Created by Ashish Patel at 2024/12/28 20:57
# leetgo: 1.4.11
# https://leetcode.com/problems/reshape-the-matrix/

"""
566. Reshape the Matrix (Easy)
In MATLAB, there is a handy function called `reshape` which can reshape an `m x n` matrix into a new
one with a different size `r x c` keeping its original data.

You are given an `m x n` matrix `mat` and two integers `r` and `c` representing the number of rows
and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-
traversing order as they were.

If the `reshape` operation with given parameters is possible and legal, output the new reshaped
matrix; Otherwise, output the original matrix.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg)

```
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg)

```
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
```

**Constraints:**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `-1000 <= mat[i][j] <= 1000`
- `1 <= r, c <= 300`

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
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
               flat.append(mat[row][col]) 
        if len(flat) != r * c:
            return mat
        result = []
        for i in range(0,len(flat), c):
            result.append(flat[i:i+c])
        return result
# @lc code=end

if __name__ == "__main__":
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    ans = Solution().matrixReshape(mat, r, c)
    print("\noutput:", serialize(ans, "integer[][]"))
