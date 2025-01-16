# Created by Ashish Patel at 2025/01/16 23:46
# leetgo: 1.4.13
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

"""
2529. Maximum Count of Positive Integer and Negative Integer (Easy)
Given an array `nums` sorted in **non-decreasing** order, return the maximum between the number of
positive integers and the number of negative integers.

- In other words, if the number of positive integers in `nums` is `pos` and the number of negative
integers is `neg`, then return the maximum of `pos` and `neg`.

**Note** that `0` is neither positive nor negative.

**Example 1:**

```
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is
3.
```

**Example 2:**

```
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is
3.
```

**Example 3:**

```
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is
4.
```

**Constraints:**

- `1 <= nums.length <= 2000`
- `-2000 <= nums[i] <= 2000`
- `nums` is sorted in a **non-decreasing order**.

**Follow up:** Can you solve the problem in `O(log(n))` time complexity?

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
    def maximumCount(self, nums: List[int]) -> int:
        negatives = []
        positives = []
        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
        return max(len(negatives), len(positives))

# @lc code=end

if __name__ == "__main__":
    nums = [-3,-2,-1,0,0,1,2]
    ans = Solution().maximumCount(nums)
    print("\noutput:", serialize(ans, "integer"))
