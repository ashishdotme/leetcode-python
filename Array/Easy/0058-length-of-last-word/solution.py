# Created by Ashish Patel at 2024/08/13 23:38
# leetgo: 1.4.7
# https://leetcode.com/problems/length-of-last-word/

"""
58. Length of Last Word (Easy)
Given a string `s` consisting of words and spaces, return the length of the **last** word in the
string.

A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

**Example 2:**

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

**Example 3:**

```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

**Constraints:**

- `1 <= s.length <= 10⁴`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

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
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLastWord(s)
    print("\noutput:", serialize(ans, "integer"))
