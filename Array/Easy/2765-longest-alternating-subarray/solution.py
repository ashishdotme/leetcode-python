# Created by Ashish Patel at 2025/01/06 20:49
# leetgo: 1.4.13
# https://leetcode.com/problems/longest-alternating-subarray/

"""
2765. Longest Alternating Subarray (Easy)
You are given a **0-indexed** integer array `nums`. A subarray `s` of length `m` is called
**alternating** if:

- `m` is greater than `1`.
- `s₁ = s₀ + 1`.
- The **0-indexed** subarray `s` looks like `[s₀, s₁, s₀, s₁,...,s₍ₘ₋₁₎ % ₂]`. In other words, `s₁ - s₀
= 1`, `s₂ - s₁ = -1`, `s₃ - s₂ = 1`, `s₄ - s₃ = -1`, and so on up to `s[m - 1] - s[m - 2] = (-1)ᵐ`.

Return the maximum length of all **alternating** subarrays present in  `nums`or  `-1` if no such
subarray exists.

A subarray is a contiguous **non-empty** sequence of elements within an array.

**Example 1:**

**Input:** nums = \[2,3,4,3,4\]

**Output:** 4

**Explanation:**

The alternating subarrays are `[2, 3]`, `[3,4]`, `[3,4,3]`, and `[3,4,3,4]`. The longest of these is
`[3,4,3,4]`, which is of length 4.

**Example 2:**

**Input:** nums = \[4,5,6\]

**Output:** 2

**Explanation:**

`[4,5]` and `[5,6]` are the only two alternating subarrays. They are both of length 2.

**Constraints:**

- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 10⁴`

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
    def alternatingSubarray(self, nums: List[int]) -> int:
        check = 1
        max_current = -1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == check:
                current += 1
                check *= -1
                max_current = max(max_current, current)
            else:
                if nums[i] - nums[i-1] == 1:
                    current = 2
                    check = -1
                else:
                    current = 1
                    check = 1
        return max_current

# @lc code=end

if __name__ == "__main__":
    nums: List[int] =  [2,3,4,3,4]
    ans = Solution().alternatingSubarray(nums)
    print("\noutput:", serialize(ans, "integer"))
