# Created by Ashish Patel at 2025/01/16 00:11
# leetgo: 1.4.13
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

"""
2133. Check if Every Row and Column Contains All Numbers (Easy)
An `n x n` matrix is **valid** if every row and every column contains **all** the integers from `1`
to `n` ( **inclusive**).

Given an `n x n` integer matrix `matrix`, return `true`if the matrix is **valid**. Otherwise, return
`false`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/12/21/example1drawio.png)

```
Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/12/21/example2drawio.png)

```
Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers
2 or 3.
Hence, we return false.
```

**Constraints:**

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 100`
- `1 <= matrix[i][j] <= n`

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
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for row in matrix:
            if not all((num + 1) in row for num in range(len(matrix))):
                return False
        cols = []
        for col in range(len(matrix[0])):
            cols.append([row[col] for row in matrix])
            
        for col in cols:
            if not all((num + 1) in col for num in range(len(col))):
                return False
        return True

# @lc code=end

if __name__ == "__main__":
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    ans = Solution().checkValid(matrix)
    print("\noutput:", serialize(ans, "boolean"))
