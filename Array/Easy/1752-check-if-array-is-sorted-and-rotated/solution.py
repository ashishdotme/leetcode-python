# Created by Ashish Patel at 2025/01/09 22:36
# leetgo: 1.4.13
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

"""
1752. Check if Array Is Sorted and Rotated (Easy)
Given an array `nums`, return `true` if the array was originally sorted in non-decreasing order, then
rotated **some** number of positions (including zero). Otherwise, return `false`.

There may be **duplicates** in the original array.

**Note:** An array `A` rotated by `x` positions results in an array `B` of the same length such that
`A[i] == B[(i+x) % A.length]`, where `%` is the modulo operation.

**Example 1:**

```
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
```

**Example 2:**

```
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
```

**Example 3:**

```
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
```

**Constraints:**

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

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
    def check(self, nums: List[int]) -> bool:
        size = len(nums)
        count = 0
        for i in range(size):
            if nums[i] > nums[(i + 1) % size]:
                count += 1
            if count > 1:
                return False
        return True

# @lc code=end

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    ans = Solution().check(nums)
    print("\noutput:", serialize(ans, "boolean"))
