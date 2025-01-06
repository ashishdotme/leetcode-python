# Created by Ashish Patel at 2025/01/05 17:21
# leetgo: 1.4.13
# https://leetcode.com/problems/max-pair-sum-in-an-array/

"""
2815. Max Pair Sum in an Array (Easy)
You are given an integer array `nums`. You have to find the **maximum** sum of a pair of numbers
from `nums` such that the **largest digit** in both numbers is equal.

For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among
them.

Return the **maximum** sum or -1 if no such pair exists.

**Example 1:**

**Input:** nums = \[112,131,411\]

**Output:**-1

**Explanation:**

Each numbers largest digit in order is \[2,3,4\].

**Example 2:**

**Input:** nums = \[2536,1613,3366,162\]

**Output:** 5902

**Explanation:**

All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

**Example 3:**

**Input:** nums = \[51,71,17,24,42\]

**Output:** 88

**Explanation:**

Each number's largest digit in order is \[5,7,7,4,4\].

So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.

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
    def maxSum(self, nums: List[int]) -> int:
        res, d = -1, DefaultDict(int)
        for num in nums:
            digit = int(max(str(num)))
            if digit in d:
                res = max(res, num + d[digit])
            d[digit] = max(num, d[digit])
        return res
        

# @lc code=end

if __name__ == "__main__":
    nums =  [2536,1613,3366,162]
    ans = Solution().maxSum(nums)
    print("\noutput:", serialize(ans, "integer"))
