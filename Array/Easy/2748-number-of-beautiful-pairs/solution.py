# Created by Ashish Patel at 2025/01/08 16:55
# leetgo: 1.4.11
# https://leetcode.com/problems/number-of-beautiful-pairs/

"""
2748. Number of Beautiful Pairs (Easy)
You are given a **0-indexed** integer array `nums`. A pair of indices `i`, `j` where `0 <= i < j <
nums.length` is called beautiful if the **first digit** of `nums[i]` and the **last digit** of
`nums[j]` are **coprime**.

Return the total number of beautiful pairs in  `nums`.

Two integers `x` and `y` are **coprime** if there is no integer greater than 1 that divides both of
them. In other words, `x` and `y` are coprime if `gcd(x, y) == 1`, where `gcd(x, y)` is the
**greatest common divisor** of `x` and `y`.

**Example 1:**

```
Input: nums = [2,5,1,4]
Output: 5
Explanation: There are 5 beautiful pairs in nums:
When i = 0 and j = 1: the first digit of nums[0] is 2, and the last digit of nums[1] is 5. We can
confirm that 2 and 5 are coprime, since gcd(2,5) == 1.
When i = 0 and j = 2: the first digit of nums[0] is 2, and the last digit of nums[2] is 1. Indeed,
gcd(2,1) == 1.
When i = 1 and j = 2: the first digit of nums[1] is 5, and the last digit of nums[2] is 1. Indeed,
gcd(5,1) == 1.
When i = 1 and j = 3: the first digit of nums[1] is 5, and the last digit of nums[3] is 4. Indeed,
gcd(5,4) == 1.
When i = 2 and j = 3: the first digit of nums[2] is 1, and the last digit of nums[3] is 4. Indeed,
gcd(1,4) == 1.
Thus, we return 5.
```

**Example 2:**

```
Input: nums = [11,21,12]
Output: 2
Explanation: There are 2 beautiful pairs:
When i = 0 and j = 1: the first digit of nums[0] is 1, and the last digit of nums[1] is 1. Indeed,
gcd(1,1) == 1.
When i = 0 and j = 2: the first digit of nums[0] is 1, and the last digit of nums[2] is 2. Indeed,
gcd(1,2) == 1.
Thus, we return 2.
```

**Constraints:**

- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 9999`
- `nums[i] % 10 != 0`

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
    def countBeautifulPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                first, second = str(nums[i]), str(nums[j])
                if math.gcd(int(first[0]), int(second[-1])) == 1:
                    result +=1
        return result
                    
            

# @lc code=end

if __name__ == "__main__":
    nums = [2,5,1,4]
    ans = Solution().countBeautifulPairs(nums)
    print("\noutput:", serialize(ans, "integer"))
