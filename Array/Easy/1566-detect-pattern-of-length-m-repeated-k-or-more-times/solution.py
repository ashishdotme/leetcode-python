# Created by Ashish Patel at 2025/01/17 15:01
# leetgo: 1.4.11
# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

"""
1566. Detect Pattern of Length M Repeated K or More Times (Easy)
Given an array of positive integers `arr`, find a pattern of length `m` that is repeated `k` or more
times.

A **pattern** is a subarray (consecutive sub-sequence) that consists of one or more values, repeated
multiple times **consecutively** without overlapping. A pattern is defined by its length and the
number of repetitions.

Return `true`if there exists a pattern of length `m`that is repeated `k`or more times, otherwise
return `false`.

**Example 1:**

```
Input: arr = [1,2,4,4,4,4], m = 1, k = 3
Output: true
Explanation: The pattern (4) of length 1 is repeated 4 consecutive times. Notice that pattern can be
repeated k or more times but not less.
```

**Example 2:**

```
Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
Output: true
Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times. Another valid pattern
(2,1) is also repeated 2 times.
```

**Example 3:**

```
Input: arr = [1,2,1,2,1,3], m = 2, k = 3
Output: false
Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of
length 2 that is repeated 3 or more times.
```

**Constraints:**

- `2 <= arr.length <= 100`
- `1 <= arr[i] <= 100`
- `1 <= m <= 100`
- `2 <= k <= 100`

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
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        patterns = {}
        for i in range(len(arr)-m):
            temp = 1
            for j in range(i, len(arr), m):
                if arr[i:i+m] == arr[j:j+m]:
                    temp += 1
            patterns[str(arr[i:i+m])] = temp
        print(patterns)
        for key, value in patterns.items():
            if value >= k:
                return True
        return False

# @lc code=end

if __name__ == "__main__":
    arr = [1,2,1,2,1,1,1,3]
    m = 2
    k = 2
    ans = Solution().containsPattern(arr, m, k)
    print("\noutput:", serialize(ans, "boolean"))
