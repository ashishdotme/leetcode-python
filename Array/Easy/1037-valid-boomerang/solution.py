# Created by Ashish Patel at 2025/01/14 16:56
# leetgo: 1.4.11
# https://leetcode.com/problems/valid-boomerang/

"""
1037. Valid Boomerang (Easy)
Given an array `points` where `points[i] = [xᵢ, yᵢ]` represents a point on the **X-Y** plane, return
`true`if these points are a **boomerang**.

A **boomerang** is a set of three points that are **all distinct** and **not in a straight line**.

**Example 1:**

```
Input: points = [[1,1],[2,3],[3,2]]
Output: true
```

**Example 2:**

```
Input: points = [[1,1],[2,2],[3,3]]
Output: false
```

**Constraints:**

- `points.length == 3`
- `points[i].length == 2`
- `0 <= xᵢ, yᵢ <= 100`

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

# @lc code=begin

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
        return area != 0

# @lc code=end

if __name__ == "__main__":
    points = [[1,1],[2,3],[3,2]]
    ans = Solution().isBoomerang(points)
    print("\noutput:", serialize(ans, "boolean"))
