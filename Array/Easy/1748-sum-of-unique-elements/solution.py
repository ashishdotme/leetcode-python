# Created by Ashish Patel at 2025/01/04 21:47
# leetgo: 1.4.13
# https://leetcode.com/problems/sum-of-unique-elements/

"""
1748. Sum of Unique Elements (Easy)
You are given an integer array `nums`. The unique elements of an array are the elements that appear
**exactly once** in the array.

Return the **sum** of all the unique elements of  `nums`.

**Example 1:**

```
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
```

**Example 2:**

```
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
```

**Example 3:**

```
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
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
    def sumOfUnique(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        sum = 0
        for key, value in map.items():
            if value == 1:
               sum += key
        return sum

# @lc code=end

if __name__ == "__main__":
    nums = [1,2,3,2]
    ans = Solution().sumOfUnique(nums)
    print("\noutput:", serialize(ans, "integer"))
