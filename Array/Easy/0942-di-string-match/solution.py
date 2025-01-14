# Created by Ashish Patel at 2025/01/13 14:40
# leetgo: 1.4.11
# https://leetcode.com/problems/di-string-match/

"""
942. DI String Match (Easy)
A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` can be
represented as a string `s` of length `n` where:

- `s[i] == 'I'` if `perm[i] < perm[i + 1]`, and
- `s[i] == 'D'` if `perm[i] > perm[i + 1]`.

Given a string `s`, reconstruct the permutation `perm` and return it. If there are multiple valid
permutations perm, return **any of them**.

**Example 1:**

```
Input: s = "IDID"
Output: [0,4,1,3,2]
```

**Example 2:**

```
Input: s = "III"
Output: [0,1,2,3]
```

**Example 3:**

```
Input: s = "DDI"
Output: [3,2,0,1]
```

**Constraints:**

- `1 <= s.length <= 10⁵`
- `s[i]` is either `'I'` or `'D'`.

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
    def diStringMatch(self, s: str) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().diStringMatch(s)
    print("\noutput:", serialize(ans, "integer[]"))
