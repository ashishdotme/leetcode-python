# Created by Ashish Patel at 2025/01/07 16:28
# leetgo: 1.4.11
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

"""
2215. Find the Difference of Two Arrays (Easy)
Given two **0-indexed** integer arrays `nums1` and `nums2`, return a list `answer`of size `2`where:

- `answer[0]`is a list of all **distinct** integers in `nums1`which are **not** present in `nums2`.
- `answer[1]`is a list of all **distinct** integers in `nums2`which are **not** present in `nums1`.

**Note** that the integers in the lists may be returned in **any** order.

**Example 1:**

```
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are
not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are
not present in nums2. Therefore, answer[1] = [4,6].
```

**Example 2:**

```
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value
is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `-1000 <= nums1[i], nums2[i] <= 1000`

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
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[], []]
        nums1count = Counter(nums1)
        nums2count = Counter(nums2)
        for num in nums1:
            if num not in nums2count and num not in result[0]:
                result[0].append(num)
        for num in nums2:
            if num not in nums1count and num not in result[1]:
                result[1].append(num)
        return result

# @lc code=end

if __name__ == "__main__":
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    ans = Solution().findDifference(nums1, nums2)
    print("\noutput:", serialize(ans, "integer[][]"))
