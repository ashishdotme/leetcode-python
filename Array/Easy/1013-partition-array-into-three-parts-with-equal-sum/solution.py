# Created by Ashish Patel at 2024/12/18 15:07
# leetgo: 1.4.11
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

"""
1013. Partition Array Into Three Parts With Equal Sum (Easy)
Given an array of integers `arr`, return `true` if we can partition the array into three **non-
empty** parts with equal sums.

Formally, we can partition the array if we can find indexes `i + 1 < j` with `(arr[0] + arr[1] + ...
+ arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length -
1])`

**Example 1:**

```
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
```

**Example 2:**

```
Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
```

**Example 3:**

```
Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
```

**Constraints:**

- `3 <= arr.length <= 5 * 10⁴`
- `-10⁴ <= arr[i] <= 10⁴`

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
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    arr = [0,2,1,-6,6,-7,9,1,2,0,1]
    ans = Solution().canThreePartsEqualSum(arr)
    print("\noutput:", serialize(ans, "boolean"))
