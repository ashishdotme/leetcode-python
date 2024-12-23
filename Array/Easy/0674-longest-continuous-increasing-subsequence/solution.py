# Created by Ashish Patel at 2024/12/17 15:23
# leetgo: 1.4.11
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

"""
674. Longest Continuous Increasing Subsequence (Easy)
Given an unsorted array of integers `nums`, return the length of the longest **continuous increasing
subsequence** (i.e. subarray). The subsequence must be **strictly** increasing.

A **continuous increasing subsequence** is defined by two indices `l` and `r` ( `l < r`) such that
it is `[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]` and for each `l <= i < r`, `nums[i] <
nums[i + 1]`.

**Example 1:**

```
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are
separated by element
4.
```

**Example 2:**

```
Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must
be strictly
increasing.
```

**Constraints:**

- `1 <= nums.length <= 10⁴`
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
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            counter = 1
            index = i
            while index < len(nums) - 1 and nums[index+1] > nums[index] :
                counter += 1  
                index += 1
            result = max(counter, result)
        return result            

# @lc code=end

if __name__ == "__main__":
    nums = [1,3,5,4,7]
    ans = Solution().findLengthOfLCIS(nums)
    print("\noutput:", serialize(ans, "integer"))
