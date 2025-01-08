# Created by Ashish Patel at 2025/01/08 11:17
# leetgo: 1.4.13
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

"""
1380. Lucky Numbers in a Matrix (Easy)
Given an `m x n` matrix of **distinct** numbers, return all **lucky numbers** in the matrix in
**any** order.

A **lucky number** is an element of the matrix such that it is the minimum element in its row and
maximum in its column.

**Example 1:**

```
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its
column.
```

**Example 2:**

```
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its
column.
```

**Example 3:**

```
Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its
column.
```

**Constraints:**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= n, m <= 50`
- `1 <= matrix[i][j] <= 10⁵`.
- All elements in the matrix are distinct.

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
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_row = []
        max_col = []
        for i in range(len(matrix)):
            min_row.append(min(matrix[i]))
        cols = []
        for col in range(len(matrix[0])):
            cols.append([row[col] for row in matrix])
        for col in cols:
            max_col.append(max(col))
        return list(set(min_row) & set(max_col))

# @lc code=end

if __name__ == "__main__":
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    ans = Solution().luckyNumbers(matrix)
    print("\noutput:", serialize(ans, "integer[]"))
