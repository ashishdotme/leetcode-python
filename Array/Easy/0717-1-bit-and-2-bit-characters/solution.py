# Created by Ashish Patel at 2025/01/03 13:24
# leetgo: 1.4.11
# https://leetcode.com/problems/1-bit-and-2-bit-characters/

"""
717. 1-bit and 2-bit Characters (Easy)
We have two special characters:

- The first character can be represented by one bit `0`.
- The second character can be represented by two bits ( `10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last character must be a one-bit
character.

**Example 1:**

```
Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
```

**Example 2:**

```
Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
```

**Constraints:**

- `1 <= bits.length <= 1000`
- `bits[i]` is either `0` or `1`.

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
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        no = 0
        while no < len(bits) - 1:
            if bits[no] == 0:
                no += 1
            else:
                no += 2
        return no == len(bits) - 1

# @lc code=end

if __name__ == "__main__":
    bits = [1,1,1,0]
    ans = Solution().isOneBitCharacter(bits)
    print("\noutput:", serialize(ans, "boolean"))
