# Created by Ashish Patel at 2024/12/13 16:15
# leetgo: 1.4.11
# https://leetcode.com/problems/longest-harmonious-subsequence/

"""
594. Longest Harmonious Subsequence (Easy)
We define a harmonious array as an array where the difference between its maximum value and its
minimum value is **exactly** `1`.

Given an integer array `nums`, return the length of its longest harmonious subsequence among all its
possible subsequences.

**Example 1:**

**Input:** nums = \[1,3,2,2,5,2,3,7\]

**Output:** 5

**Explanation:**

The longest harmonious subsequence is `[3,2,2,2,3]`.

**Example 2:**

**Input:** nums = \[1,2,3,4\]

**Output:** 2

**Explanation:**

The longest harmonious subsequences are `[1,2]`, `[2,3]`, and `[3,4]`, all of which have a length of
2.

**Example 3:**

**Input:** nums = \[1,1,1,1\]

**Output:** 0

**Explanation:**

No harmonic subsequence exists.

**Constraints:**

- `1 <= nums.length <= 2 * 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`

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
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        max_length = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in freq.keys():
            if num + 1 in freq:
                current_length = freq[num] + freq[num + 1]
                max_length = max(max_length, current_length)
        return max_length
# @lc code=end

if __name__ == "__main__":
    nums = [1,3,2,2,5,2,3,7]
    ans = Solution().findLHS(nums)
    print("\noutput:", serialize(ans, "integer"))
