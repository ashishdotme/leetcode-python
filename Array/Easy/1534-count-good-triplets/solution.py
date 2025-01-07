# Created by Ashish Patel at 2025/01/07 15:03
# leetgo: 1.4.11
# https://leetcode.com/problems/count-good-triplets/

"""
1534. Count Good Triplets (Easy)
Given an array of integers `arr`, and three integers `a`, `b` and `c`. You need to find the number
of good triplets.

A triplet `(arr[i], arr[j], arr[k])` is **good** if the following conditions are true:

- `0 <= i < j < k < arr.length`
- `|arr[i] - arr[j]| <= a`
- `|arr[j] - arr[k]| <= b`
- `|arr[i] - arr[k]| <= c`

Where `|x|` denotes the absolute value of `x`.

Return the number of good triplets.

**Example 1:**

```
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
```

**Example 2:**

```
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
```

**Constraints:**

- `3 <= arr.length <= 100`
- `0 <= arr[i] <= 1000`
- `0 <= a, b, c <= 1000`

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
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        size = len(arr)
        for i in range(size-2):
            for j in range(i+1, size -1):
                for k in range(j+1, size):
                    if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] -arr[k]) <= b )and (abs(arr[i] - arr[k]) <= c):
                        result += 1
        return result

# @lc code=end

if __name__ == "__main__":
    arr = [3,0,1,1,9,7]
    a = 7
    b = 2
    c = 3
    ans = Solution().countGoodTriplets(arr, a, b, c)
    print("\noutput:", serialize(ans, "integer"))
