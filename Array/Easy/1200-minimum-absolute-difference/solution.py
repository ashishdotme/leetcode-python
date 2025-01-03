# Created by Ashish Patel at 2025/01/03 13:10
# leetgo: 1.4.11
# https://leetcode.com/problems/minimum-absolute-difference/

"""
1200. Minimum Absolute Difference (Easy)
Given an array of **distinct** integers `arr`, find all pairs of elements with the minimum absolute
difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair `[a, b]` follows

- `a, b` are from `arr`
- `a < b`
- `b - a` equals to the minimum absolute difference of any two elements in `arr`

**Example 1:**

```
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in
ascending order.
```

**Example 2:**

```
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
```

**Example 3:**

```
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
```

**Constraints:**

- `2 <= arr.length <= 10⁵`
- `-10⁶ <= arr[i] <= 10⁶`

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
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        minDifference = math.inf
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < minDifference:
                minDifference = arr[i+1] - arr[i]

        for i in range(0,len(arr) - 1, 1):
            if arr[i + 1] - arr[i] == minDifference:
                result.append([arr[i], arr[i+1]])
        return result

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = [4,2,1,3]
    ans = Solution().minimumAbsDifference(arr)
    print("\noutput:", serialize(ans, "integer[][]"))
