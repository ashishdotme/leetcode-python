# Created by Ashish Patel at 2025/01/04 13:00
# leetgo: 1.4.13
# https://leetcode.com/problems/smallest-range-i/

"""
908. Smallest Range I (Easy)
You are given an integer array `nums` and an integer `k`.

In one operation, you can choose any index `i` where `0 <= i < nums.length` and change `nums[i]` to
`nums[i] + x` where `x` is an integer from the range `[-k, k]`. You can apply this operation **at
most once** for each index `i`.

The **score** of `nums` is the difference between the maximum and minimum elements in `nums`.

Return the minimum **score** of  `nums` after applying the mentioned operation at most once for each
index in it.

**Example 1:**

```
Input: nums = [1], k = 0
Output: 0
Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
```

**Example 2:**

```
Input: nums = [0,10], k = 2
Output: 6
Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
```

**Example 3:**

```
Input: nums = [1,3,6], k = 3
Output: 0
Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.
```

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `0 <= nums[i] <= 10⁴`
- `0 <= k <= 10⁴`

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
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        left = min(nums) + k
        right = max(max(nums) - k, left)
        return right - left

# @lc code=end

if __name__ == "__main__":
    nums = [0,10]
    k = 2
    ans = Solution().smallestRangeI(nums, k)
    print("\noutput:", serialize(ans, "integer"))
