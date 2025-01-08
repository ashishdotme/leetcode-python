# Created by Ashish Patel at 2025/01/08 15:56
# leetgo: 1.4.11
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/

"""
2475. Number of Unequal Triplets in Array (Easy)
You are given a **0-indexed** array of positive integers `nums`. Find the number of triplets `(i, j,
k)` that meet the following conditions:

- `0 <= i < j < k < nums.length`
- `nums[i]`, `nums[j]`, and `nums[k]` are **pairwise distinct**.

  - In other words, `nums[i] != nums[j]`, `nums[i] != nums[k]`, and `nums[j] != nums[k]`.

Return the number of triplets that meet the conditions.

**Example 1:**

```
Input: nums = [4,4,2,4,3]
Output: 3
Explanation: The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.
```

**Example 2:**

```
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: No triplets meet the conditions so we return 0.
```

**Constraints:**

- `3 <= nums.length <= 100`
- `1 <= nums[i] <= 1000`

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
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(0,len(nums)):
          for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
              if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                count += 1
        return count

# @lc code=end

if __name__ == "__main__":
    nums = [4,4,2,4,3]
    ans = Solution().unequalTriplets(nums)
    print("\noutput:", serialize(ans, "integer"))
