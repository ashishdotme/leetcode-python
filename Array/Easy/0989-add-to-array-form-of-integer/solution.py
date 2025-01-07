# Created by Ashish Patel at 2025/01/06 11:27
# leetgo: 1.4.13
# https://leetcode.com/problems/add-to-array-form-of-integer/

"""
989. Add to Array-Form of Integer (Easy)
The **array-form** of an integer `num` is an array representing its digits in left to right order.

- For example, for `num = 1321`, the array form is `[1,3,2,1]`.

Given `num`, the **array-form** of an integer, and an integer `k`, return the **array-form** of the
integer `num + k`.

**Example 1:**

```
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
```

**Example 2:**

```
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
```

**Example 3:**

```
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
```

**Constraints:**

- `1 <= num.length <= 10⁴`
- `0 <= num[i] <= 9`
- `num` does not contain any leading zeros except for the zero itself.
- `1 <= k <= 10⁴`

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
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        digit = 0
        for i in num:
            digit = digit * 10 + i
            
        total = digit + k
        result = []
        while(total != 0):
            result.append(total%10)
            total=total//10
        return result[::-1]
# @lc code=end

if __name__ == "__main__":
    num = [1,2,0,0]
    k = 34
    ans = Solution().addToArrayForm(num, k)
    print("\noutput:", serialize(ans, "integer[]"))
