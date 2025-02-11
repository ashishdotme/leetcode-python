# Created by Ashish Patel at 2025/01/23 16:36
# leetgo: 1.4.11
# https://leetcode.com/problems/maximum-subarray/

"""
53. Maximum Subarray (Medium)
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

**Example 2:**

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

**Example 3:**

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the
**divide and conquer** approach, which is more subtle.

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
    def maxSubArray(self, nums: List[int]) -> int:
        total_sum = nums[0]
        curr_sum = nums[0]
        
        for num in nums[1:]:
            curr_sum = max(curr_sum, curr_sum + num)
            total_sum = max(total_sum, curr_sum)
        
        return total_sum

# @lc code=end

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ans = Solution().maxSubArray(nums)
    print("\noutput:", serialize(ans, "integer"))
