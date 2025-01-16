# Created by Ashish Patel at 2025/01/14 20:48
# leetgo: 1.4.13
# https://leetcode.com/problems/relative-sort-array/

"""
1122. Relative Sort Array (Easy)
Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2`
are also in `arr1`.

Sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in
`arr2`. Elements that do not appear in `arr2` should be placed at the end of `arr1` in **ascending**
order.

**Example 1:**

```
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
```

**Example 2:**

```
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
```

**Constraints:**

- `1 <= arr1.length, arr2.length <= 1000`
- `0 <= arr1[i], arr2[i] <= 1000`
- All the elements of `arr2` are **distinct**.
- Each `arr2[i]` is in `arr1`.

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
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        remaining = []
        counts = Counter(arr1)
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                remaining.append(arr1[i])
        for i in range(len(arr2)):
            if arr2[i] in arr1:
                result.extend([arr2[i]] * counts[arr2[i]])
        remaining.sort()
        return result + remaining

# @lc code=end

if __name__ == "__main__":
    arr1 = [28,6,22,8,44,17]
    arr2 = [22,28,8,6]
    ans = Solution().relativeSortArray(arr1, arr2)
    print("\noutput:", serialize(ans, "integer[]"))
