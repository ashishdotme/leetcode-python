# Created by Ashish Patel at 2024/12/28 21:48
# leetgo: 1.4.13
# https://leetcode.com/problems/range-addition-ii/

"""
598. Range Addition II (Easy)
You are given an `m x n` matrix `M` initialized with all `0`'s and an array of operations `ops`,
where `ops[i] = [aᵢ, bᵢ]` means `M[x][y]` should be incremented by one for all `0 <= x < aᵢ` and `0
<= y < bᵢ`.

Count and return the number of maximum integers in the matrix after performing all the operations.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/02/ex1.jpg)

```
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
```

**Example 2:**

```
Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
```

**Example 3:**

```
Input: m = 3, n = 3, ops = []
Output: 9
```

**Constraints:**

- `1 <= m, n <= 4 * 10⁴`
- `0 <= ops.length <= 10⁴`
- `ops[i].length == 2`
- `1 <= aᵢ <= m`
- `1 <= bᵢ <= n`

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
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        for i,j in ops:
            m = min(m, i)
            n = min(n, j)
        
        return m * n

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ops: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxCount(m, n, ops)
    print("\noutput:", serialize(ans, "integer"))
