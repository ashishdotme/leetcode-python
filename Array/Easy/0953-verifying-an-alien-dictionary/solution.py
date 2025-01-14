# Created by Ashish Patel at 2025/01/13 14:50
# leetgo: 1.4.11
# https://leetcode.com/problems/verifying-an-alien-dictionary/

"""
953. Verifying an Alien Dictionary (Easy)
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a
different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return
`true` if and only if the given `words` are sorted lexicographically in this alien language.

**Example 1:**

```
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
```

**Example 2:**

```
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence
is unsorted.
```

**Example 3:**

```
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the
blank character which is less than any other character (More info).
```

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- `order.length == 26`
- All characters in `words[i]` and `order` are English lowercase letters.

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
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = { ch: i for i, ch in enumerate(order)}
        prev = list(hm[ch] for ch in words[0])
        for i in range(len(words)):
            curr = list(hm[ch] for ch in words[i])
            if curr < prev:
                return False
            prev = curr
        return True

# @lc code=end

if __name__ == "__main__":
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    ans = Solution().isAlienSorted(words, order)
    print("\noutput:", serialize(ans, "boolean"))
