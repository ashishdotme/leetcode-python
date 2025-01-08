# Created by Ashish Patel at 2025/01/08 14:57
# leetgo: 1.4.11
# https://leetcode.com/problems/minimum-distance-to-the-target-element/

"""
1848. Minimum Distance to the Target Element (Easy)
Given an integer array `nums` **(0-indexed)** and two integers `target` and `start`, find an index
`i` such that `nums[i] == target` and `abs(i - start)` is **minimized**. Note that `abs(x)` is the
absolute value of `x`.

Return `abs(i - start)`.

It is **guaranteed** that `target` exists in `nums`.

**Example 1:**

```
Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
```

**Example 2:**

```
Input: nums = [1], target = 1, start = 0
Output: 0
Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.
```

**Example 3:**

```
Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
Output: 0
Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10⁴`
- `0 <= start < nums.length`
- `target` is in `nums`.

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
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = math.inf
        for i, num in enumerate(nums):
            if num == target:
                result = min(result,abs(i - start))
        return result

# @lc code=end

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    target = 5
    start = 3
    ans = Solution().getMinDistance(nums, target, start)
    print("\noutput:", serialize(ans, "integer"))
