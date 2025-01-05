# Created by Ashish Patel at 2025/01/05 10:54
# leetgo: 1.4.13
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

"""
961. N-Repeated Element in Size 2N Array (Easy)
You are given an integer array `nums` with the following properties:

- `nums.length == 2 * n`.
- `nums` contains `n + 1` **unique** elements.
- Exactly one element of `nums` is repeated `n` times.

Return the element that is repeated  `n` times.

**Example 1:**

```
Input: nums = [1,2,3,3]
Output: 3
```

**Example 2:**

```
Input: nums = [2,1,2,5,3,2]
Output: 2
```

**Example 3:**

```
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
```

**Constraints:**

- `2 <= n <= 5000`
- `nums.length == 2 * n`
- `0 <= nums[i] <= 10⁴`
- `nums` contains `n + 1` **unique** elements and one of them is repeated exactly `n` times.

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
    def repeatedNTimes(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        for key, value in map.items():
            if value == len(nums)/2:
                return key
        return map

# @lc code=end

if __name__ == "__main__":
    nums = [2,1,2,5,3,2]
    ans = Solution().repeatedNTimes(nums)
    print("\noutput:", serialize(ans, "integer"))
