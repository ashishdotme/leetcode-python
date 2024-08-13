# Created by Ashish Patel at 2024/08/13 19:16
# leetgo: 1.4.7
# https://leetcode.com/problems/is-subsequence/

"""
392. Is Subsequence (Easy)
Given two strings `s` and `t`, return `true` if  `s` is a **subsequence** of  `t`, or  `false`
otherwise.

A **subsequence** of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

**Example 1:**

```
Input: s = "abc", t = "ahbgdc"
Output: true
```

**Example 2:**

```
Input: s = "axc", t = "ahbgdc"
Output: false
```

**Constraints:**

- `0 <= s.length <= 100`
- `0 <= t.length <= 10⁴`
- `s` and `t` consist only of lowercase English letters.

**Follow up:** Suppose there are lots of incoming `s`, say `s₁, s₂, ..., sₖ` where `k >= 10⁹`, and
you want to check one by one to see if `t` has its subsequence. In this scenario, how would you
change your code?

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
    def isSubsequence(self, s: str, t: str) -> bool:
        i , j = 0, 0
        while i < len(s) and j < len(t):
            if(s[i] == t[j]):
                i+= 1
            j+= 1
        return i == len(s)
        
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().isSubsequence(s, t)
    print("\noutput:", serialize(ans, "boolean"))
