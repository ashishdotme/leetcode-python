# Created by Ashish Patel at 2024/12/23 15:55
# leetgo: 1.4.11
# https://leetcode.com/problems/maximum-height-of-a-triangle/

"""
3200. Maximum Height of a Triangle (Easy)
You are given two integers `red` and `blue` representing the count of red and blue colored balls.
You have to arrange these balls to form a triangle such that the 1 row will have 1 ball, the 2 row
will have 2 balls, the 3 row will have 3 balls, and so on.

All the balls in a particular row should be the **same** color, and adjacent rows should have
**different** colors.

Return the **maximum** height of the triangle that can be achieved.

**Example 1:**

**Input:** red = 2, blue = 4

**Output:** 3

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/06/16/brb.png)

The only possible arrangement is shown above.

**Example 2:**

**Input:** red = 2, blue = 1

**Output:** 2

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/06/16/br.png)

The only possible arrangement is shown above.

**Example 3:**

**Input:** red = 1, blue = 1

**Output:** 1

**Example 4:**

**Input:** red = 10, blue = 1

**Output:** 2

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/06/16/br.png)

The only possible arrangement is shown above.

**Constraints:**

- `1 <= red, blue <= 100`

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
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def calculate_height(a, b, flag):
            height = 0
            while(height % 2== 0 and a > height or height % 2== 1 and b > height):
                if height % 2 == 0:
                    a -= height + 1
                else:
                    b -= height + 1
                height += 1
            return height
        return max(calculate_height(red, blue, True), calculate_height(blue,red, False))

# @lc code=end

if __name__ == "__main__":
    # red = 10, blue = 10
    red: int = 2
    blue: int = 4
    ans = Solution().maxHeightOfTriangle(red, blue)
    print("\noutput:", serialize(ans, "integer"))
