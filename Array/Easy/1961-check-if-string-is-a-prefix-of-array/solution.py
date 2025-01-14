# Created by Ashish Patel at 2025/01/10 15:28
# leetgo: 1.4.11
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

"""
1961. Check If String Is a Prefix of Array (Easy)
Given a string `s` and an array of strings `words`, determine whether `s` is a **prefix string** of
`words`.

A string `s` is a **prefix string** of `words` if `s` can be made by concatenating the first `k`
strings in `words` for some **positive** `k` no larger than `words.length`.

Return `true` if  `s` is a **prefix string** of  `words`, or  `false` otherwise.

**Example 1:**

```
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.
```

**Example 2:**

```
Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.
```

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- `1 <= s.length <= 1000`
- `words[i]` and `s` consist of only lowercase English letters.

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
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        index = 0
        temp = ''
        while(index < len(words)):
            temp += words[index]
            if temp == s:
                return True
            index += 1
        return False                

# @lc code=end

if __name__ == "__main__":
    s = "iloveleetcode"
    words = ["i","love","leetcode","apples"]
    ans = Solution().isPrefixString(s, words)
    print("\noutput:", serialize(ans, "boolean"))
