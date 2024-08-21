# Created by Ashish Patel at 2024/08/21 13:20
# leetgo: 1.4.7
# https://leetcode.com/problems/majority-element/

"""
169. Majority Element (Easy)
Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the
majority element always exists in the array.

**Example 1:**

```
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5 * 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

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
    def majorityElement(self, nums: List[int]) -> int:
        count , result = 0, 0
        for num in nums:
            if count == 0:
                result = num
            if result == num:
                count += 1
            else:
                count -= 1
        return result

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().majorityElement(nums)
    print("\noutput:", serialize(ans, "integer"))
