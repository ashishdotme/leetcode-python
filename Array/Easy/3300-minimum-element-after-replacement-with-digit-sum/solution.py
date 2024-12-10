# Created by Ashish Patel at 2024/11/19 16:27
# leetgo: 1.4.11
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

"""
3300. Minimum Element After Replacement With Digit Sum (Easy)
You are given an integer array `nums`.

You replace each element in `nums` with the **sum** of its digits.

Return the **minimum** element in `nums` after all replacements.

**Example 1:**

**Input:** nums = \[10,12,13,14\]

**Output:** 1

**Explanation:**

`nums` becomes `[1, 3, 4, 5]` after all replacements, with minimum element 1.

**Example 2:**

**Input:** nums = \[1,2,3,4\]

**Output:** 1

**Explanation:**

`nums` becomes `[1, 2, 3, 4]` after all replacements, with minimum element 1.

**Example 3:**

**Input:** nums = \[999,19,199\]

**Output:** 10

**Explanation:**

`nums` becomes `[27, 10, 19]` after all replacements, with minimum element 10.

**Constraints:**

- `1 <= nums.length <= 100`
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
import leetcode as lc

# @lc code=begin

class Solution:
    def minElement(self, nums: List[int]) -> int:
        minSum = math.inf
        for i in range(len(nums)):
            sum = 0
            n = nums[i]
            while( n != 0):
                sum += n % 10
                n = n // 10
            minSum = min(minSum, sum)
        return minSum


# @lc code=end

if __name__ == "__main__":
    # nums: List[int] = deserialize("List[int]", read_line())
    nums = [10, 12,13 ,45]
    ans = Solution().minElement(nums)
    print("\noutput:", serialize(ans, "integer"))
