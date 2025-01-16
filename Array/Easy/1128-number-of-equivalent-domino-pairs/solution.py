# Created by Ashish Patel at 2025/01/14 21:07
# leetgo: 1.4.13
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

"""
1128. Number of Equivalent Domino Pairs (Easy)
Given a list of `dominoes`, `dominoes[i] = [a, b]` is **equivalent to** `dominoes[j] = [c, d]` if
and only if either ( `a == c` and `b == d`), or ( `a == d` and `b == c`) \- that is, one domino can
be rotated to be equal to another domino.

Return the number of pairs  `(i, j)` for which  `0 <= i < j < dominoes.length`, and  `dominoes[i]`
is **equivalent to** `dominoes[j]`.

**Example 1:**

```
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
```

**Example 2:**

```
Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
```

**Constraints:**

- `1 <= dominoes.length <= 4 * 10⁴`
- `dominoes[i].length == 2`
- `1 <= dominoes[i][j] <= 9`

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
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        result = 0
        dict = DefaultDict(int)
        for first, second in dominoes:
            pair = (min(first,second), max(first, second))
            if pair in dict:
                result += dict[pair]
            dict[pair] += 1
        return result

# @lc code=end

if __name__ == "__main__":
    dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    ans = Solution().numEquivDominoPairs(dominoes)
    print("\noutput:", serialize(ans, "integer"))
