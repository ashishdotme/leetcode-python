# Created by Ashish Patel at 2024/12/10 15:15
# leetgo: 1.4.11
# https://leetcode.com/problems/teemo-attacking/

"""
495. Teemo Attacking (Easy)
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets
poisoned for a exactly `duration` seconds. More formally, an attack at second `t` will mean Ashe is
poisoned during the **inclusive** time interval `[t, t + duration - 1]`. If Teemo attacks again
**before** the poison effect ends, the timer for it is **reset**, and the poison effect will end
`duration` seconds after the new attack.

You are given a **non-decreasing** integer array `timeSeries`, where `timeSeries[i]` denotes that
Teemo attacks Ashe at second `timeSeries[i]`, and an integer `duration`.

Return the **total** number of seconds that Ashe is poisoned.

**Example 1:**

```
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
```

**Example 2:**

```
Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds
2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
```

**Constraints:**

- `1 <= timeSeries.length <= 10⁴`
- `0 <= timeSeries[i], duration <= 10⁷`
- `timeSeries` is sorted in **non-decreasing** order.

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
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        if len(timeSeries) == 1:
            return duration
        for i in range(len(timeSeries)):
            if i < len(timeSeries) - 1 and timeSeries[i + 1] <= timeSeries[i] + duration - 1:
                result += timeSeries[i+1] - timeSeries[i]
            else:
                result += duration
        return result

# @lc code=end

if __name__ == "__main__":
    timeSeries = [1,2]
    duration = 2
    ans = Solution().findPoisonedDuration(timeSeries, duration)
    print("\noutput:", serialize(ans, "integer"))
