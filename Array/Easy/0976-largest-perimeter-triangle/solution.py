# Created by Ashish Patel at 2025/01/14 14:54
# leetgo: 1.4.11
# https://leetcode.com/problems/largest-perimeter-triangle/

"""
976. Largest Perimeter Triangle (Easy)
Given an integer array `nums`, return the largest perimeter of a triangle with a non-zero area,
formed from three of these lengths. If it is impossible to form any triangle of a non-zero area,
return `0`.

**Example 1:**

```
Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
```

**Example 2:**

```
Input: nums = [1,2,1,10]
Output: 0
Explanation:
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
```

**Constraints:**

- `3 <= nums.length <= 10⁴`
- `1 <= nums[i] <= 10⁶`

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
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
# @lc code=end

if __name__ == "__main__":
    nums = [2,1,2]
    ans = Solution().largestPerimeter(nums)
    print("\noutput:", serialize(ans, "integer"))
