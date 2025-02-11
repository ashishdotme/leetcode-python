# Created by Ashish Patel at 2025/01/17 14:27
# leetgo: 1.4.11
# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

"""
1560. Most Visited Sector in  a Circular Track (Easy)
Given an integer `n` and an integer array `rounds`. We have a circular track which consists of `n`
sectors labeled from `1` to `n`. A marathon will be held on this track, the marathon consists of `m`
rounds. The `iᵗʰ` round starts at sector `rounds[i - 1]` and ends at sector `rounds[i]`. For example,
round 1 starts at sector `rounds[0]` and ends at sector `rounds[1]`

Return an array of the most visited sectors sorted in **ascending** order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise
direction (See the first example).

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/14/tmp.jpg)

```
Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]
Explanation: The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors.
Sectors 3 and 4 are visited only once.
```

**Example 2:**

```
Input: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
Output: [2]
```

**Example 3:**

```
Input: n = 7, rounds = [1,3,5,7]
Output: [1,2,3,4,5,6,7]
```

**Constraints:**

- `2 <= n <= 100`
- `1 <= m <= 100`
- `rounds.length == m + 1`
- `1 <= rounds[i] <= n`
- `rounds[i] != rounds[i + 1]` for `0 <= i < m`

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
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        d = {i: 0 for i in range(1, n+1)}
        for i in range(len(rounds)-1):
            start = rounds[i]
            end = rounds[i+1]
            while(start != end):
                if start > n:
                    start = 1
                else:
                    d[start] += 1
                    start += 1
        d[end] += 1
        sorted_d = sorted(d.items(), key= lambda x : x[1], reverse=True)
        result = []
        for key, value in sorted_d:
            if value == sorted_d[0][1]:
                result.append(key)
        return result

# @lc code=end

if __name__ == "__main__":
    n = 4
    rounds = [1,3,1,2]
    ans = Solution().mostVisited(n, rounds)
    print("\noutput:", serialize(ans, "integer[]"))
