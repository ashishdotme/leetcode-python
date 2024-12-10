# Created by Ashish Patel at 2024/11/12 16:51
# leetgo: 1.4.11
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

"""
3349. Adjacent Increasing Subarrays Detection I (Easy)
Given an array `nums` of `n` integers and an integer `k`, determine whether there exist **two**
**adjacent** subarrays of length `k` such that both subarrays are **strictly** **increasing**.
Specifically, check if there are **two** subarrays starting at indices `a` and `b` ( `a < b`),
where:

- Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly increasing**.
- The subarrays must be **adjacent**, meaning `b = a + k`.

Return `true` if it is possible to find **two** such subarrays, and `false` otherwise.

**Example 1:**

**Input:** nums = \[2,5,7,8,9,2,3,4,3,1\], k = 3

**Output:** true

**Explanation:**

- The subarray starting at index `2` is `[7, 8, 9]`, which is strictly increasing.
- The subarray starting at index `5` is `[2, 3, 4]`, which is also strictly increasing.
- These two subarrays are adjacent, so the result is `true`.

**Example 2:**

**Input:** nums = \[1,2,3,4,4,4,4,5,6,7\], k = 5

**Output:** false

**Constraints:**

- `2 <= nums.length <= 100`
- `1 < 2 * k <= nums.length`
- `-1000 <= nums[i] <= 1000`

"""

import bisect
import collections
import functools
import heapq
import itertools
import math
import operator
import string
from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def isIncreasing(self, subArray: List[int]) -> bool:
        for i in range(len(subArray) - 1):
            if subArray[i + 1] > subArray[i]:
                continue
            else:
                return False
        return True

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2 * k:
            return False
        for i in range(len(nums) - 2 * k + 1):
            if self.isIncreasing(nums[i : i + k]) and self.isIncreasing(
                nums[i + k : i + 2 * k]
            ):
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().hasIncreasingSubarrays(nums, k)
    print("\noutput:", serialize(ans, "boolean"))
