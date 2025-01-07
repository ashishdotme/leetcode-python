# Created by Ashish Patel at 2025/01/06 10:45
# leetgo: 1.4.13
# https://leetcode.com/problems/find-the-town-judge/

"""
997. Find the Town Judge (Easy)
In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people
is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties **1** and **2**.

You are given an array `trust` where `trust[i] = [aᵢ, bᵢ]` representing that the person labeled `aᵢ`
trusts the person labeled `bᵢ`. If a trust relationship does not exist in `trust` array, then such a
trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return  `-1`
otherwise.

**Example 1:**

```
Input: n = 2, trust = [[1,2]]
Output: 2
```

**Example 2:**

```
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```

**Example 3:**

```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

**Constraints:**

- `1 <= n <= 1000`
- `0 <= trust.length <= 10⁴`
- `trust[i].length == 2`
- All the pairs of `trust` are **unique**.
- `aᵢ != bᵢ`
- `1 <= aᵢ, bᵢ <= n`

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
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = [0] * (n + 1)
        trusted = [0]  * (n + 1)
        
        for info in trust:
            trusting[info[0]] += 1
            trusted[info[1]] += 1

        result = -1
        
        for i in range(1, len(trusting)):
            if trusting[i] == 0 and trusted[i] == n - 1:
                result = i
                
        return result

# @lc code=end

if __name__ == "__main__":
    n = 3
    trust = [[1,3],[2,3]]
    ans = Solution().findJudge(n, trust)
    print("\noutput:", serialize(ans, "integer"))
