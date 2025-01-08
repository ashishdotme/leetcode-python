# Created by Ashish Patel at 2025/01/08 10:43
# leetgo: 1.4.13
# https://leetcode.com/problems/two-out-of-three/

"""
2032. Two Out of Three (Easy)
Given three integer arrays `nums1`, `nums2`, and `nums3`, return a **distinct** array containing all
the values that are present in **at least two** out of the three arrays. You may return the values
in **any** order.

**Example 1:**

```
Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.
```

**Example 2:**

```
Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.
```

**Example 3:**

```
Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.
```

**Constraints:**

- `1 <= nums1.length, nums2.length, nums3.length <= 100`
- `1 <= nums1[i], nums2[j], nums3[k] <= 100`

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
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq = Counter()
        for num in nums1, nums2, nums3:
            freq.update(set(num))
        result = []
        for key, val in freq.items():
            if val >=2:
                result.append(key)
        return result
        

# @lc code=end

if __name__ == "__main__":
    nums1 = [1,1,3,2]
    nums2 = [2,3]
    nums3 = [3]
    ans = Solution().twoOutOfThree(nums1, nums2, nums3)
    print("\noutput:", serialize(ans, "integer[]"))
