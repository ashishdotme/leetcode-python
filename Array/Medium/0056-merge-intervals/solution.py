# Created by Ashish Patel at 2025/01/14 14:03
# leetgo: 1.4.11
# https://leetcode.com/problems/merge-intervals/

"""
56. Merge Intervals (Medium)
Given an array of `intervals` where `intervals[i] = [startᵢ, endᵢ]`, merge all overlapping
intervals, and return an array of the non-overlapping intervals that cover all the intervals in the
input.

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**Constraints:**

- `1 <= intervals.length <= 10⁴`
- `intervals[i].length == 2`
- `0 <= startᵢ <= endᵢ <= 10⁴`

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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = sorted(intervals)
        result = []
        i = 0
        j = i + 1
        while j < len(s):
            if s[i][-1] >= s[j][0]:
                s[j] = [min(s[i][0], s[j][0]), max(s[i][1], s[j][1])]
            else:
                result.append(s[i])
            j += 1
            i += 1
        result.append(s[i])
        return result

# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = [[1,3],[2,6],[8,10],[15,18]]
    ans = Solution().merge(intervals)
    print("\noutput:", serialize(ans, "integer[][]"))
