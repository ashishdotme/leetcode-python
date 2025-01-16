# Created by Ashish Patel at 2025/01/16 23:49
# leetgo: 1.4.13
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

"""
2441. Largest Positive Integer That Exists With Its Negative (Easy)
Given an integer array `nums` that **does not contain** any zeros, find **the largest positive**
integer `k` such that `-k` also exists in the array.

Return the positive integer  `k`. If there is no such integer, return `-1`.

**Example 1:**

```
Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
```

**Example 2:**

```
Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger
value.
```

**Example 3:**

```
Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- `nums[i] != 0`

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
    def findMaxK(self, nums: List[int]) -> int:
        result = -1
        for i in range(len(nums)):
            target = -nums[i]
            if target in nums:
                result = max(result, nums[i])
        return result

# @lc code=end

if __name__ == "__main__":
    nums = [-1,10,6,7,-7,1]
    ans = Solution().findMaxK(nums)
    print("\noutput:", serialize(ans, "integer"))
