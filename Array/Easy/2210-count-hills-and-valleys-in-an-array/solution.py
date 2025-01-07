# Created by Ashish Patel at 2025/01/07 16:43
# leetgo: 1.4.11
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

"""
2210. Count Hills and Valleys in an Array (Easy)
You are given a **0-indexed** integer array `nums`. An index `i` is part of a **hill** in `nums` if
the closest non-equal neighbors of `i` are smaller than `nums[i]`. Similarly, an index `i` is part of
a **valley** in `nums` if the closest non-equal neighbors of `i` are larger than `nums[i]`. Adjacent
indices `i` and `j` are part of the **same** hill or valley if `nums[i] == nums[j]`.

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on **both**
the left and right of the index.

Return _the number of hills and valleys in_ `nums`.

**Example 1:**

```
Input: nums = [2,4,1,1,6,5]
Output: 3
Explanation:
At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a
valley.
At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a
hill.
At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a
valley.
At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a
valley, but note that it is part of the same valley as index 2.
At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a
hill.
At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a
valley.
There are 3 hills and valleys so we return 3.
```

**Example 2:**

```
Input: nums = [6,6,5,5,4,1]
Output: 0
Explanation:
At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill nor a
valley.
At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill nor a
valley.
At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 2 is
neither a hill nor a valley.
At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 3 is
neither a hill nor a valley.
At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index 4 is
neither a hill nor a valley.
At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill nor a
valley.
There are 0 hills and valleys so we return 0.
```

**Constraints:**

- `3 <= nums.length <= 100`
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
import leetcode as lc

# @lc code=begin

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0
        left, right = 0, 1
        while right < len(nums) -1:
            if (nums[left] < nums[right] and nums[right] > nums[right +1]) or (nums[left] > nums[right] and nums[right] < nums[right+1]):
                result += 1
                left = right
            right += 1
        return result
                

# @lc code=end

if __name__ == "__main__":
    nums = [2,4,1,1,6,5]
    ans = Solution().countHillValley(nums)
    print("\noutput:", serialize(ans, "integer"))
