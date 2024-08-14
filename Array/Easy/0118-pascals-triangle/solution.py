# Created by Ashish Patel at 2024/08/14 16:43
# leetgo: 1.4.7
# https://leetcode.com/problems/pascals-triangle/

"""
118. Pascal's Triangle (Easy)
Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

**Example 1:**

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Example 2:**

```
Input: numRows = 1
Output: [[1]]
```

**Constraints:**

- `1 <= numRows <= 30`

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
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        result = [[1], [1, 1]]
        last = [1, 1]
        for i in range(numRows-2):
            temp = [1]
            for j in range(0, len(last) - 1):
                temp.append(last[j] + last[j+1])
            temp.append(1)
            last = temp
            result.append(last)
        return result
# @lc code=end

if __name__ == "__main__":
    numRows: int = deserialize("int", read_line())
    ans = Solution().generate(numRows)
    print("\noutput:", serialize(ans, "integer[][]"))
