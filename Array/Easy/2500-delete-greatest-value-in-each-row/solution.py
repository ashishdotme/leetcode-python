# Created by Ashish Patel at 2025/01/08 21:17
# leetgo: 1.4.13
# https://leetcode.com/problems/delete-greatest-value-in-each-row/

"""
2500. Delete Greatest Value in Each Row (Easy)
You are given an `m x n` matrix `grid` consisting of positive integers.

Perform the following operation until `grid` becomes empty:

- Delete the element with the greatest value from each row. If multiple such elements exist, delete
any of them.
- Add the maximum of deleted elements to the answer.

**Note** that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/10/19/q1ex1.jpg)

```
Input: grid = [[1,2,4],[3,3,1]]
Output: 8
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that,
there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the
answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the
answer.
The final answer = 4 + 3 + 1 = 8.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/10/19/q1ex2.jpg)

```
Input: grid = [[10]]
Output: 10
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.
```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j] <= 100`

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
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        
        sum = 0
        for col in range(len(grid[0])):
            sum += max([row[col] for row in grid])
        
        return sum
# @lc code=end

if __name__ == "__main__":
    grid = [[1,2,4],[3,3,1]]
    ans = Solution().deleteGreatestValue(grid)
    print("\noutput:", serialize(ans, "integer"))
