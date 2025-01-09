# Created by Ashish Patel at 2025/01/09 14:57
# leetgo: 1.4.11
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

"""
1588. Sum of All Odd Length Subarrays (Easy)
Given an array of positive integers `arr`, return the sum of all possible **odd-length subarrays** of
`arr`.

A **subarray** is a contiguous subsequence of the array.

**Example 1:**

```
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
```

**Example 2:**

```
Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
```

**Example 3:**

```
Input: arr = [10,11,12]
Output: 66
```

**Constraints:**

- `1 <= arr.length <= 100`
- `1 <= arr[i] <= 1000`

**Follow up:**

Could you solve this problem in O(n) time complexity?

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
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for size in range(1,len(arr)+1,2):
            left = 0
            while size <= len(arr):
                total += sum(arr[left:size])
                left += 1
                size +=1 
        return total

# @lc code=end

if __name__ == "__main__":
    arr = [1,4,2,5,3]
    ans = Solution().sumOddLengthSubarrays(arr)
    print("\noutput:", serialize(ans, "integer"))
