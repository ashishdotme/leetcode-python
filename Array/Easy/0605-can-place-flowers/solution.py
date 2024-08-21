# Created by Ashish Patel at 2024/08/21 11:49
# leetgo: 1.4.7
# https://leetcode.com/problems/can-place-flowers/

"""
605. Can Place Flowers (Easy)
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers
cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means
not empty, and an integer `n`, return `true`if `n`new flowers can be planted in the
`flowerbed`without violating the no-adjacent-flowers rule and `false`otherwise.

**Example 1:**

```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

**Example 2:**

```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

**Constraints:**

- `1 <= flowerbed.length <= 2 * 10⁴`
- `flowerbed[i]` is `0` or `1`.
- There are no two adjacent flowers in `flowerbed`.
- `0 <= n <= flowerbed.length`

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
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    break
        return n == 0

# @lc code=end

if __name__ == "__main__":
    flowerbed: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().canPlaceFlowers(flowerbed, n)
    print("\noutput:", serialize(ans, "boolean"))
