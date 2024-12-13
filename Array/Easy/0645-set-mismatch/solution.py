# Created by Ashish Patel at 2024/12/13 16:36
# leetgo: 1.4.11
# https://leetcode.com/problems/set-mismatch/

"""
645. Set Mismatch (Easy)
You have a set of integers `s`, which originally contains all the numbers from `1` to `n`.
Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the
set, which results in **repetition of one** number and **loss of another** number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an
array.

**Example 1:**

```
Input: nums = [1,2,2,4]
Output: [2,3]
```

**Example 2:**

```
Input: nums = [1,1]
Output: [1,2]
```

**Constraints:**

- `2 <= nums.length <= 10⁴`
- `1 <= nums[i] <= 10⁴`

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
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = -1
        dup = -1
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = dict.get(nums[i], 0) + 1
            if dict[nums[i]] == 2:
                dup = nums[i]
                break
            
        missing = list(set(list(range(1, len(nums) + 1))) - set(nums))[0]
        return[dup, missing]

# @lc code=end

if __name__ == "__main__":
    nums = [3,2,2]
    ans = Solution().findErrorNums(nums)
    print("\noutput:", serialize(ans, "integer[]"))
