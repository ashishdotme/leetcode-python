# Created by Ashish Patel at 2025/01/14 22:04
# leetgo: 1.4.13
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

"""
1160. Find Words That Can Be Formed by Characters (Easy)
You are given an array of strings `words` and a string `chars`.

A string is **good** if it can be formed by characters from `chars` (each character can only be used
once).

Return the sum of lengths of all good strings in words.

**Example 1:**

```
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
```

**Example 2:**

```
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
```

**Constraints:**

- `1 <= words.length <= 1000`
- `1 <= words[i].length, chars.length <= 100`
- `words[i]` and `chars` consist of lowercase English letters.

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
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        result = []
        for word in words:
            word_count = Counter(word)
            if all(word_count[char] <= chars_count[char] for char in word):
                result.append(len(word))
        return sum(result)
# @lc code=end

if __name__ == "__main__":
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    ans = Solution().countCharacters(words, chars)
    print("\noutput:", serialize(ans, "integer"))
