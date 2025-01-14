# Created by Ashish Patel at 2025/01/13 16:12
# leetgo: 1.4.11
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
34. Find First and Last Position of Element in Sorted Array (Medium)
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending
position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**Example 2:**

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

**Example 3:**

```
Input: nums = [], target = 0
Output: [-1,-1]
```

**Constraints:**

- `0 <= nums.length <= 10⁵`
- `-10⁹ <= nums[i] <= 10⁹`
- `nums` is a non-decreasing array.
- `-10⁹ <= target <= 10⁹`

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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]

# @lc code=end

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    ans = Solution().searchRange(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
