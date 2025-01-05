# Created by Ashish Patel at 2025/01/04 17:52
# leetgo: 1.4.13
# https://leetcode.com/problems/kth-missing-positive-number/

"""
1539. Kth Missing Positive Number (Easy)
Given an array `arr` of positive integers sorted in a **strictly increasing order**, and an integer
`k`.

Return the `kᵗʰ`**positive** integer that is **missing** from this array.

**Example 1:**

```
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5ᵗʰ missing positive
integer is 9.
```

**Example 2:**

```
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2ⁿᵈ missing positive integer is 6.
```

**Constraints:**

- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 1000`
- `1 <= k <= 1000`
- `arr[i] < arr[j]` for `1 <= i < j <= arr.length`

**Follow up:**

Could you solve this problem in less than O(n) complexity?

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
    def findKthPositive(self, arr: List[int], k: int) -> int:
        result = []
        i = 0
        n = 1
        while k > 0:
            if i < len(arr) and arr[i] == n:
                i += 1
                n += 1
            else:
                k -= 1
                result.append(n)
                n += 1
        return result.pop()

# @lc code=end


if __name__ == "__main__":
    arr = [2,3,4,7,11]
    k = 5
    ans = Solution().findKthPositive(arr, k)
    print("\noutput:", serialize(ans, "integer"))
