# Created by Ashish Patel at 2024/08/12 16:04
# leetgo: 1.4.7
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

"""
1299. Replace Elements with Greatest Element on Right Side (Easy)
Given an array `arr`, replace every element in that array with the greatest element among the
elements to its right, and replace the last element with `-1`.

After doing so, return the array.

**Example 1:**

```
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
```

**Example 2:**

```
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
```

**Constraints:**

- `1 <= arr.length <= 10⁴`
- `1 <= arr[i] <= 10⁵`

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
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(arr[i], max_num)
            arr[i] = max_num
            max_num = new_max
        return arr


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().replaceElements(arr)
    print("\noutput:", serialize(ans, "integer[]"))
