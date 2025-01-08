# Created by Ashish Patel at 2025/01/08 20:38
# leetgo: 1.4.13
# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

"""
2605. Form Smallest Number From Two Digit Arrays (Easy)
Given two arrays of **unique** digits `nums1` and `nums2`, return the **smallest** number that
contains **at least** one digit from each array.

**Example 1:**

```
Input: nums1 = [4,1,3], nums2 = [5,7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be
proven that 15 is the smallest number we can have.
```

**Example 2:**

```
Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
Output: 3
Explanation: The number 3 contains the digit 3 which exists in both arrays.
```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 9`
- `1 <= nums1[i], nums2[i] <= 9`
- All digits in each array are **unique**.

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
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1set = set(nums1)
        nums2set = set(nums2)
        intersection = nums1set & nums2set
        if len(intersection) > 0:
            return min(list(intersection))
        min_num1 = min(nums1set)
        min_num2 = min(nums2set)
        if min_num1 < min_num2:
            return int(str(min_num1) + str(min_num2))
        else:
            return int(str(min_num2) + str(min_num1))
        

# @lc code=end

if __name__ == "__main__":
    nums1 = [4,1,3]
    nums2 = [5,7]
    ans = Solution().minNumber(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
