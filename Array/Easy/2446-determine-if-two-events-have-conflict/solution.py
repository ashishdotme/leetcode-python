# Created by Ashish Patel at 2025/01/08 16:14
# leetgo: 1.4.11
# https://leetcode.com/problems/determine-if-two-events-have-conflict/

"""
2446. Determine if Two Events Have Conflict (Easy)
You are given two arrays of strings that represent two inclusive events that happened **on the same
day**, `event1` and `event2`, where:

- `event1 = [startTime₁, endTime₁]` and
- `event2 = [startTime₂, endTime₂]`.

Event times are valid 24 hours format in the form of `HH:MM`.

A **conflict** happens when two events have some non-empty intersection (i.e., some moment is common
to both events).

Return `true` if there is a conflict between two events. Otherwise, return  `false`.

**Example 1:**

```
Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.
```

**Example 2:**

```
Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.
```

**Example 3:**

```
Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.
```

**Constraints:**

- `event1.length == event2.length == 2`
- `event1[i].length == event2[i].length == 5`
- `startTime₁ <= endTime₁`
- `startTime₂ <= endTime₂`
- All the event times follow the `HH:MM` format.

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
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if event2[0] < event1[0]:
            event1, event2 = event2, event1
        if event2[0] > event1[1]:
            return False
        else:
            return True

# @lc code=end

if __name__ == "__main__":
    event1 = ["01:00","02:00"]
    event2 = ["01:20","03:00"]
    ans = Solution().haveConflict(event1, event2)
    print("\noutput:", serialize(ans, "boolean"))
