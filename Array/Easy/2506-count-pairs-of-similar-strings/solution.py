# Created by Ashish Patel at 2025/01/04 20:21
# leetgo: 1.4.13
# https://leetcode.com/problems/count-pairs-of-similar-strings/

"""
2506. Count Pairs Of Similar Strings (Easy)
You are given a **0-indexed** string array `words`.

Two strings are **similar** if they consist of the same characters.

- For example, `"abca"` and `"cba"` are similar since both consist of characters `'a'`, `'b'`, and
`'c'`.
- However, `"abacba"` and `"bcfd"` are not similar since they do not consist of the same characters.

Return the number of pairs  `(i, j)` such that  `0 <= i < j <= word.length - 1` and the two strings
`words[i]` and  `words[j]` are similar.

**Example 1:**

```
Input: words = ["aba","aabb","abcd","bac","aabc"]
Output: 2
Explanation: There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'.
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'.
```

**Example 2:**

```
Input: words = ["aabb","ab","ba"]
Output: 3
Explanation: There are 3 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'.
- i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
- i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.
```

**Example 3:**

```
Input: words = ["nba","cba","dba"]
Output: 0
Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.
```

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consist of only lowercase English letters.

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
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i, w1 in enumerate(words):
            for w2 in words[i+1:]:
                if set(w1) == set(w2):
                    count += 1
                    
        return count

# @lc code=end

if __name__ == "__main__":
    words = ["aabb","ab","ba"]
    ans = Solution().similarPairs(words)
    print("\noutput:", serialize(ans, "integer"))
