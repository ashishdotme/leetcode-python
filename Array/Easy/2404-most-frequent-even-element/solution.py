# Created by Ashish Patel at 2025/01/08 15:49
# leetgo: 1.4.11
# https://leetcode.com/problems/most-frequent-even-element/

"""
2404. Most Frequent Even Element (Easy)
Given an integer array `nums`, return the most frequent even element.

If there is a tie, return the **smallest** one. If there is no such element, return `-1`.

**Example 1:**

```
Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
```

**Example 2:**

```
Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
```

**Example 3:**

```
Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
```

**Constraints:**

- `1 <= nums.length <= 2000`
- `0 <= nums[i] <= 10⁵`

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
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = Counter(nums).most_common()
        counts.sort(key = lambda x: x[0])
        counts.sort(key = lambda x: x[1], reverse=True)
        for key, value in counts:
            if key % 2 == 0:
                return key
        return -1
            

# @lc code=end

if __name__ == "__main__":
    nums = [0,1,2,2,4,4,1]
    ans = Solution().mostFrequentEven(nums)
    print("\noutput:", serialize(ans, "integer"))
