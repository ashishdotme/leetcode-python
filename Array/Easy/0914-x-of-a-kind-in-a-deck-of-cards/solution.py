# Created by Ashish Patel at 2025/01/04 13:20
# leetgo: 1.4.13
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

"""
914. X of a Kind in a Deck of Cards (Easy)
You are given an integer array `deck` where `deck[i]` represents the number written on the `iᵗʰ`
card.

Partition the cards into **one or more groups** such that:

- Each group has **exactly** `x` cards where `x > 1`, and
- All the cards in one group have the same integer written on them.

Return `true` if such partition is possible, or  `false` otherwise.

**Example 1:**

```
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
```

**Example 2:**

```
Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
```

**Constraints:**

- `1 <= deck.length <= 10⁴`
- `0 <= deck[i] < 10⁴`

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
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cache = Counter(deck)
        if len(cache) == 1:
            return cache[deck[0]] > 1
        
        x = cache[deck[0]]
        
        for num in cache.values():
            x = math.gcd(x, num)
        
        return  x > 1

# @lc code=end

if __name__ == "__main__":
    deck = [1,2,3,4,4,3,2,1]
    ans = Solution().hasGroupsSizeX(deck)
    print("\noutput:", serialize(ans, "boolean"))
