# Created by Ashish Patel at 2025/01/05 12:31
# leetgo: 1.4.13
# https://leetcode.com/problems/find-subarrays-with-equal-sum/

"""
2395. Find Subarrays With Equal Sum (Easy)
Given a **0-indexed** integer array `nums`, determine whether there exist **two** subarrays of length
`2` with **equal** sum. Note that the two subarrays must begin at **different** indices.

Return `true` if these subarrays exist, and  `false` otherwise.

A **subarray** is a contiguous non-empty sequence of elements within an array.

**Example 1:**

```
Input: nums = [4,2,4]
Output: true
Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.
```

**Example 2:**

```
Input: nums = [1,2,3,4,5]
Output: false
Explanation: No two subarrays of size 2 have the same sum.
```

**Example 3:**

```
Input: nums = [0,0,0]
Output: true
Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0.
Note that even though the subarrays have the same content, the two subarrays are considered
different because they are in different positions in the original array.
```

**Constraints:**

- `2 <= nums.length <= 1000`
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

# @lc code=begin

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        cache = set()
        for i in range(len(nums)-1):
            sum = nums[i] + nums[i+1]
            if sum in cache:
                return True
            cache.add(sum)
        return False
                

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findSubarrays(nums)
    print("\noutput:", serialize(ans, "boolean"))
