# Created by Ashish Patel at 2025/01/07 11:03
# leetgo: 1.4.13
# https://leetcode.com/problems/sort-array-by-increasing-frequency/

"""
1636. Sort Array by Increasing Frequency (Easy)
Given an array of integers `nums`, sort the array in **increasing** order based on the frequency of
the values. If multiple values have the same frequency, sort them in **decreasing** order.

Return the sorted array.

**Example 1:**

```
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
```

**Example 2:**

```
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
```

**Example 3:**

```
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
```

**Constraints:**

- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

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
    def frequencySort(self, nums: List[int]) -> List[int]:
        count=Counter(nums).most_common()
        count.sort(key= lambda x: x[0], reverse=True)
        count.sort(key= lambda x: x[1])
        result = []
        for num in count:
            a,b = num
            result.extend([a]*b)
        return result

# @lc code=end

if __name__ == "__main__":
    nums = [1,1,2,2,2,3]
    ans = Solution().frequencySort(nums)
    print("\noutput:", serialize(ans, "integer[]"))
