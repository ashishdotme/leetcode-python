# Created by Ashish Patel at 2025/01/07 14:12
# leetgo: 1.4.11
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

"""
2099. Find Subsequence of Length K With the Largest Sum (Easy)
You are given an integer array `nums` and an integer `k`. You want to find a **subsequence** of
`nums` of length `k` that has the **largest** sum.

Return**any** such subsequence as an integer array of length  `k`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements.

**Example 1:**

```
Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
```

**Example 2:**

```
Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation:
The subsequence has the largest sum of -1 + 3 + 4 = 6.
```

**Example 3:**

```
Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7.
Another possible subsequence is [4, 3].
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `-10⁵ <= nums[i] <= 10⁵`
- `1 <= k <= nums.length`

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
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp = nums.copy()
        temp.sort(reverse=True)
        temp = temp[:k]
        print(temp)
        result = []
        cnt = Counter(temp)
        for num in nums:
            if num in temp and len(result) < k and result.count(num) < cnt[num]:
                result.append(num)
        return result

# @lc code=end

if __name__ == "__main__":
    nums = [-16,-13,8,16,35,-17,30,-8,34,-2,-29,-35,15,13,-30,-34,6,15,28,-23,34,28,-24,15,-17,10,31,32,-3,-36,19,31,-5,-21,-33,-18,-23,-37,-15,12,-28,-40,1,38,38,-38,33,-35,-28,-40,4,-15,-29,-33,-18,-9,-29,20,1,36,-8,23,-34,16,-7,13,39,38,7,-7,-10,30,9,26,27,-37,-18,-25,14,-36,23,28,-15,35,-9,1]
    k = 8
    ans = Solution().maxSubsequence(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
    #[35,34,38,38,36,39,38,35]