# Created by Ashish Patel at 2025/01/03 16:02
# leetgo: 1.4.11
# https://leetcode.com/problems/largest-triangle-area/

"""
812. Largest Triangle Area (Easy)
Given an array of points on the **X-Y** plane `points` where `points[i] = [xᵢ, yᵢ]`, return the area
of the largest triangle that can be formed by any three different points. Answers within `10⁻⁵` of
the actual answer will be accepted.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png)

```
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
```

**Example 2:**

```
Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
```

**Constraints:**

- `3 <= points.length <= 50`
- `-50 <= xᵢ, yᵢ <= 50`
- All the given points are **unique**.

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
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calc(point1, point2, point3):
            x1, y1 = point1
            x2, y2 = point2
            x3, y3 = point3
            return abs(1/2 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))
        
        n = len(points)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    res = max(res, calc(points[i], points[j], points[k]))
        return res

# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    ans = Solution().largestTriangleArea(points)
    print("\noutput:", serialize(ans, "double"))
