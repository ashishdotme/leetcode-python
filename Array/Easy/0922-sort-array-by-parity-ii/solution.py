# Created by Ashish Patel at 2025/01/13 14:28
# leetgo: 1.4.11
# https://leetcode.com/problems/sort-array-by-parity-ii/

"""
922. Sort Array By Parity II (Easy)
Given an array of integers `nums`, half of the integers in `nums` are **odd**, and the other half
are **even**.

Sort the array so that whenever `nums[i]` is odd, `i` is **odd**, and whenever `nums[i]` is even,
`i` is **even**.

Return any answer array that satisfies this condition.

**Example 1:**

```
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
```

**Example 2:**

```
Input: nums = [2,3]
Output: [2,3]
```

**Constraints:**

- `2 <= nums.length <= 2 * 10⁴`
- `nums.length` is even.
- Half of the integers in `nums` are even.
- `0 <= nums[i] <= 1000`

**Follow Up:** Could you solve it in-place?

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
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = []
        odd = []
        even = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even.pop(0))
            else:
                result.append(odd.pop(0))
        return result

# @lc code=end

if __name__ == "__main__":
    nums = [4,2,5,7]
    ans = Solution().sortArrayByParityII(nums)
    print("\noutput:", serialize(ans, "integer[]"))
