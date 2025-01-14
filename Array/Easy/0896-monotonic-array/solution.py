# Created by Ashish Patel at 2025/01/13 14:00
# leetgo: 1.4.11
# https://leetcode.com/problems/monotonic-array/

"""
896. Monotonic Array (Easy)
An array is **monotonic** if it is either monotone increasing or monotone decreasing.

An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array `nums` is
monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array `nums`, return `true` if the given array is monotonic, or  `false` otherwise.

**Example 1:**

```
Input: nums = [1,2,2,3]
Output: true
```

**Example 2:**

```
Input: nums = [6,5,4,4]
Output: true
```

**Example 3:**

```
Input: nums = [1,3,2]
Output: false
```

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `-10⁵ <= nums[i] <= 10⁵`

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
    def isMonotonic(self, nums: List[int]) -> bool:
        decreasing = True
        increasing = True
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                increasing = False
            elif nums[i-1] < nums[i]:
                decreasing = False
        
        return increasing or decreasing
                

# @lc code=end

if __name__ == "__main__":
    nums = [6,5,4,4]
    ans = Solution().isMonotonic(nums)
    print("\noutput:", serialize(ans, "boolean"))
