# Created by Ashish Patel at 2025/01/15 15:19
# leetgo: 1.4.13
# https://leetcode.com/problems/rank-transform-of-an-array/

"""
1331. Rank Transform of an Array (Easy)
Given an array of integers `arr`, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

- Rank is an integer starting from 1.
- The larger the element, the larger the rank. If two elements are equal, their rank must be the
same.
- Rank should be as small as possible.

**Example 1:**

```
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the
third smallest.
```

**Example 2:**

```
Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
```

**Example 3:**

```
Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
```

**Constraints:**

- `0 <= arr.length <= 10⁵`
- `-10⁹ <= arr[i] <= 10⁹`

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
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))
        ranks = {}
        
        for i in range(len(sorted_arr)):
            ranks[sorted_arr[i]] = i + 1
        
        
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        
        return arr

# @lc code=end

if __name__ == "__main__":
    arr = [37,12,28,9,100,56,80,5,12]
    ans = Solution().arrayRankTransform(arr)
    print("\noutput:", serialize(ans, "integer[]"))
