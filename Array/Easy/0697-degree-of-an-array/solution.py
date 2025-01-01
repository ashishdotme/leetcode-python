# Created by Ashish Patel at 2024/12/30 15:53
# leetgo: 1.4.11
# https://leetcode.com/problems/degree-of-an-array/

"""
697. Degree of an Array (Easy)
Given a non-empty array of non-negative integers `nums`, the **degree** of this array is defined as
the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of `nums`, that has the
same degree as `nums`.

**Example 1:**

```
Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
```

**Example 2:**

```
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
```

**Constraints:**

- `nums.length` will be between 1 and 50,000.
- `nums[i]` will be an integer between 0 and 49,999.

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
    def findShortestSubArray(self, nums: List[int]) -> int:
        dt = DefaultDict(list)
        for i, n in enumerate(nums):
            dt[n].append(i)
            
        degree = max([len(v) for v in dt.values()])
        result = len(nums)
        for v in dt.values():
            if len(v) == degree:
                result = min(result, v[-1]-v[0]+1)
        return result 

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = [1,2,2,3,1,4,2]
    ans = Solution().findShortestSubArray(nums)
    print("\noutput:", serialize(ans, "integer"))
