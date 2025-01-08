# Created by Ashish Patel at 2025/01/08 15:47
# leetgo: 1.4.11
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

"""
1967. Number of Strings That Appear as Substrings in Word (Easy)
Given an array of strings `patterns` and a string `word`, return the **number** of strings in
`patterns` that exist as a **substring** in  `word`.

A **substring** is a contiguous sequence of characters within a string.

**Example 1:**

```
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.
```

**Example 2:**

```
Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
Explanation:
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.
```

**Example 3:**

```
Input: patterns = ["a","a","a"], word = "ab"
Output: 3
Explanation: Each of the patterns appears as a substring in word "ab".
```

**Constraints:**

- `1 <= patterns.length <= 100`
- `1 <= patterns[i].length <= 100`
- `1 <= word.length <= 100`
- `patterns[i]` and `word` consist of lowercase English letters.

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
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count    

# @lc code=end

if __name__ == "__main__":
    patterns = ["a","abc","bc","d"]
    word = "abc"
    ans = Solution().numOfStrings(patterns, word)
    print("\noutput:", serialize(ans, "integer"))
