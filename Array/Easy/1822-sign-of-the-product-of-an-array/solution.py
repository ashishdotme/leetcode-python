# Created by Ashish Patel at 2025/01/10 15:03
# leetgo: 1.4.11
# https://leetcode.com/problems/sign-of-the-product-of-an-array/

"""
1822. Sign of the Product of an Array (Easy)
Implement a function `signFunc(x)` that returns:

- `1` if `x` is positive.
- `-1` if `x` is negative.
- `0` if `x` is equal to `0`.

You are given an integer array `nums`. Let `product` be the product of all values in the array
`nums`.

Return `signFunc(product)`.

**Example 1:**

```
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
```

**Example 2:**

```
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
```

**Example 3:**

```
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `-100 <= nums[i] <= 100`

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
    def arraySign(self, nums: List[int]) -> int:
        total = 1
        for num in nums:
            total *= num
        if total < 0:
            return -1
        elif total > 0:
            return 1
        else:
            return 0

# @lc code=end

if __name__ == "__main__":
    nums = [-1,-2,-3,-4,3,2,1]
    ans = Solution().arraySign(nums)
    print("\noutput:", serialize(ans, "integer"))
