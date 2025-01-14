# Created by Ashish Patel at 2025/01/14 14:43
# leetgo: 1.4.11
# https://leetcode.com/problems/interval-list-intersections/

"""
986. Interval List Intersections (Medium)
You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] =
[startᵢ, endᵢ]` and `secondList[j] = [startⱼ, endⱼ]`. Each list of intervals is pairwise
**disjoint** and in **sorted order**.

Return the intersection of these two interval lists.

A **closed interval** `[a, b]` (with `a <= b`) denotes the set of real numbers `x` with `a <= x <=
b`.

The **intersection** of two closed intervals is a set of real numbers that are either empty or
represented as a closed interval. For example, the intersection of `[1, 3]` and `[2, 4]` is `[2,
3]`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/01/30/interval1.png)

```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

**Example 2:**

```
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
```

**Constraints:**

- `0 <= firstList.length, secondList.length <= 1000`
- `firstList.length + secondList.length >= 1`
- `0 <= startᵢ < endᵢ <= 10⁹`
- `endᵢ < startᵢ₊₁`
- `0 <= startⱼ < endⱼ <= 10⁹ `
- `endⱼ < startⱼ₊₁`

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
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    firstList: List[List[int]] = deserialize("List[List[int]]", read_line())
    secondList: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().intervalIntersection(firstList, secondList)
    print("\noutput:", serialize(ans, "integer[][]"))
