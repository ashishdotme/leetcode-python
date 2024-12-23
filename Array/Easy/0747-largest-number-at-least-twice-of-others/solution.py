# Created by Ashish Patel at 2024/12/17 15:48
# leetgo: 1.4.11
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

"""
747. Largest Number At Least Twice of Others (Easy)
You are given an integer array `nums` where the largest integer is **unique**.

Determine whether the largest element in the array is **at least twice** as much as every other
number in the array. If it is, return the **index** of the largest element, or return  `-1`
otherwise.

**Example 1:**

```
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
```

**Example 2:**

```
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
```

**Constraints:**

- `2 <= nums.length <= 50`
- `0 <= nums[i] <= 100`
- The largest element in `nums` is unique.

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
    def dominantIndex(self, nums: List[int]) -> int:
        first_max, second_max = -1, -1
        for i in range(len(nums)):
            if nums[i] > first_max and nums[i] > second_max:
                second_max = first_max
                first_max = nums[i]
                
            if nums[i] < first_max and nums[i] > second_max:
                second_max = nums[i]
        if first_max >= second_max * 2:
            return nums.index(first_max)
        else:
            return -1

# @lc code=end

if __name__ == "__main__":
    nums = [0,0,3,2]
    ans = Solution().dominantIndex(nums)
    print("\noutput:", serialize(ans, "integer"))
