# Created by Ashish Patel at 2025/01/04 18:20
# leetgo: 1.4.13
# https://leetcode.com/problems/three-consecutive-odds/

"""
1550. Three Consecutive Odds (Easy)
Given an integer array `arr`, return `true` if there are three consecutive odd numbers in the array.
Otherwise, return `false`.

**Example 1:**

```
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
```

**Example 2:**

```
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
```

**Constraints:**

- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 1000`

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
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
                    

# @lc code=end

if __name__ == "__main__":
    arr = [1,2,34,3,4,5,7,23,12]
    ans = Solution().threeConsecutiveOdds(arr)
    print("\noutput:", serialize(ans, "boolean"))
