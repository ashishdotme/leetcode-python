# Created by Ashish Patel at 2025/01/16 11:39
# leetgo: 1.4.13
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

"""
2357. Make Array Zero by Subtracting Equal Amounts (Easy)
You are given a non-negative integer array `nums`. In one operation, you must:

- Choose a positive integer `x` such that `x` is less than or equal to the **smallest non-zero**
element in `nums`.
- Subtract `x` from every **positive** element in `nums`.

Return the **minimum** number of operations to make every element in  `nums` equal to  `0`.

**Example 1:**

```
Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
```

**Example 2:**

```
Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
```

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

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
    def minimumOperations(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] == 0 or nums[i] in d:
                continue
            else:
                d[nums[i]] = 1 
        return len(d)

# @lc code=end

if __name__ == "__main__":
    nums = [1,5,0,3,5]
    ans = Solution().minimumOperations(nums)
    print("\noutput:", serialize(ans, "integer"))
