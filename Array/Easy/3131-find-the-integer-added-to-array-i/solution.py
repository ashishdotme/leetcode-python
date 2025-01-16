# Created by Ashish Patel at 2025/01/16 18:38
# leetgo: 1.4.13
# https://leetcode.com/problems/find-the-integer-added-to-array-i/

"""
3131. Find the Integer Added to Array I (Easy)
You are given two arrays of equal length, `nums1` and `nums2`.

Each element in `nums1` has been increased (or decreased in the case of negative) by an integer,
represented by the variable `x`.

As a result, `nums1` becomes **equal** to `nums2`. Two arrays are considered **equal** when they
contain the same integers with the same frequencies.

Return the integer `x`.

**Example 1:**

**Input:** nums1 = \[2,6,4\], nums2 = \[9,7,5\]

**Output:** 3

**Explanation:**

The integer added to each element of `nums1` is 3.

**Example 2:**

**Input:** nums1 = \[10\], nums2 = \[5\]

**Output:**-5

**Explanation:**

The integer added to each element of `nums1` is -5.

**Example 3:**

**Input:** nums1 = \[1,1,1,1\], nums2 = \[1,1,1,1\]

**Output:** 0

**Explanation:**

The integer added to each element of `nums1` is 0.

**Constraints:**

- `1 <= nums1.length == nums2.length <= 100`
- `0 <= nums1[i], nums2[i] <= 1000`
- The test cases are generated in a way that there is an integer `x` such that `nums1` can become
equal to `nums2` by adding `x` to each element of `nums1`.

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
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        return nums2[0] - nums1[0]

# @lc code=end

if __name__ == "__main__":
    nums1 = [2,6,4]
    nums2 = [9,7,5]
    ans = Solution().addedInteger(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
