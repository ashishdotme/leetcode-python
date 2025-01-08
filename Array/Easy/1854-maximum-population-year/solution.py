# Created by Ashish Patel at 2025/01/08 15:09
# leetgo: 1.4.11
# https://leetcode.com/problems/maximum-population-year/

"""
1854. Maximum Population Year (Easy)
You are given a 2D integer array `logs` where each `logs[i] = [birthᵢ, deathᵢ]` indicates the birth
and death years of the `iᵗʰ` person.

The **population** of some year `x` is the number of people alive during that year. The `iᵗʰ` person
is counted in year `x`'s population if `x` is in the **inclusive** range `[birthᵢ, deathᵢ - 1]`. Note
that the person is **not** counted in the year that they die.

Return the **earliest** year with the **maximum population**.

**Example 1:**

```
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
```

**Example 2:**

```
Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation:
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.
```

**Constraints:**

- `1 <= logs.length <= 100`
- `1950 <= birthᵢ < deathᵢ <= 2050`

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
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * (abs(2050-1950) + 1)
        for birth, death in logs:
            population[birth - 1950] += 1
            population[death - 1950] -= 1
        for i in range(1,len(population)):
            population[i] += population[i-1]
        max_population = max(population)
        return population.index(max_population) + 1950

# @lc code=end

if __name__ == "__main__":
    logs = [[1950,1961],[1960,1971],[1970,1981]]
    ans = Solution().maximumPopulation(logs)
    print("\noutput:", serialize(ans, "integer"))
