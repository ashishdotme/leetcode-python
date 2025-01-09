# Created by Ashish Patel at 2024/12/18 14:50
# leetgo: 1.4.11
# https://leetcode.com/problems/valid-mountain-array/

"""
941. Valid Mountain Array (Easy)
Given an array of integers `arr`, return `true` if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:

  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i] `
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

![](https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png)

**Example 1:**

```
Input: arr = [2,1]
Output: false
```

**Example 2:**

```
Input: arr = [3,5,5]
Output: false
```

**Example 3:**

```
Input: arr = [0,3,2,1]
Output: true
```

**Constraints:**

- `1 <= arr.length <= 10⁴`
- `0 <= arr[i] <= 10⁴`

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
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
          return False
        peak = arr.index(max(arr))
        if(peak == 0 or peak == len(arr) - 1):
          return False
        for i in range(peak-1):
          if arr[i] >= arr[i+1]:
            return False
        for i in range(peak, len(arr) - 1):
          if arr[i] <= arr[i+1]:
            return False
        return True
        
        

# @lc code=end

if __name__ == "__main__":
    arr = [0,3,2,1]
    ans = Solution().validMountainArray(arr)
    print("\noutput:", serialize(ans, "boolean"))
