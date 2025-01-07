# Created by Ashish Patel at 2025/01/07 10:40
# leetgo: 1.4.13
# https://leetcode.com/problems/find-closest-number-to-zero/

"""
2239. Find Closest Number to Zero (Easy)
Given an integer array `nums` of size `n`, return the number with the value **closest** to  `0` in
`nums`. If there are multiple answers, return the number with the **largest** value.

**Example 1:**

```
Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
```

**Example 2:**

```
Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
```

**Constraints:**

- `1 <= n <= 1000`
- `-10⁵ <= nums[i] <= 10⁵`

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
    def findClosestNumber(self, nums: List[int]) -> int:
        result = math.inf
        for num in nums:
            if abs(num) < abs(result):
                result = num
        if abs(result) in nums:
            return abs(result)
        return result         

# @lc code=end

if __name__ == "__main__":
    nums = [-4,-2,1,4,8]
    ans = Solution().findClosestNumber(nums)
    print("\noutput:", serialize(ans, "integer"))
