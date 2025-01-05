# Created by Ashish Patel at 2025/01/05 11:20
# leetgo: 1.4.13
# https://leetcode.com/problems/find-common-characters/

"""
1002. Find Common Characters (Easy)
Given a string array `words`, return an array of all characters that show up in all strings within
the  `words` (including duplicates). You may return the answer in **any order**.

**Example 1:**

```
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
```

**Example 2:**

```
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
```

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of lowercase English letters.

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
    def commonChars(self, words: List[str]) -> List[str]:
        counts = Counter(words[0])
        print(counts)
        for word in words[1:]:
            counts &= Counter(word)
        result = []
        for char, count in counts.items():
            result.extend([char]*count)
        return result
# @lc code=end

if __name__ == "__main__":
    words = ["bella","label","roller"]
    ans = Solution().commonChars(words)
    print("\noutput:", serialize(ans, "string[]"))
