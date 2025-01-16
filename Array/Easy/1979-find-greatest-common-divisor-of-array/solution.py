# Created by Ashish Patel at 2025/01/15 00:11
# leetgo: 1.4.13
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

"""
1979. Find Greatest Common Divisor of Array (Easy)
Given an integer array `nums`, returnthe **greatest common divisor** of the smallest number and
largest number in  `nums`.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides
both numbers.

**Example 1:**

```
Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
```

**Example 2:**

```
Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
```

**Example 3:**

```
Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
```

**Constraints:**

- `2 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`

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
    def findGCD(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)
        return math.gcd(min_num, max_num)

# @lc code=end

if __name__ == "__main__":
    nums = [2,5,6,9,10]
    ans = Solution().findGCD(nums)
    print("\noutput:", serialize(ans, "integer"))
