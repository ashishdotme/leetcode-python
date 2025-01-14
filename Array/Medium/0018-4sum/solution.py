# Created by Ashish Patel at 2025/01/13 15:12
# leetgo: 1.4.11
# https://leetcode.com/problems/4sum/

"""
18. 4Sum (Medium)
Given an array `nums` of `n` integers, return an array of all the **unique** quadruplets `[nums[a],
nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- `a`, `b`, `c`, and `d` are **distinct**.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in **any order**.

**Example 1:**

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

**Example 2:**

```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

**Constraints:**

- `1 <= nums.length <= 200`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`

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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i]  == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, len(nums) - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif curr_sum < target:
                        left+= 1
                    else:
                        right -=1
        return result
# @lc code=end       

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    ans = Solution().fourSum(nums, target)
    print("\noutput:", serialize(ans, "integer[][]"))
