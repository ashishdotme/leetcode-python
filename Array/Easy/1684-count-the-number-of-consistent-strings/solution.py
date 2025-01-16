# Created by Ashish Patel at 2025/01/15 23:41
# leetgo: 1.4.13
# https://leetcode.com/problems/count-the-number-of-consistent-strings/

"""
1684. Count the Number of Consistent Strings (Easy)
You are given a string `allowed` consisting of **distinct** characters and an array of strings
`words`. A string is **consistent** if all characters in the string appear in the string `allowed`.

Return the number of **consistent** strings in the array  `words`.

**Example 1:**

```
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
```

**Example 2:**

```
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
```

**Example 3:**

```
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
```

**Constraints:**

- `1 <= words.length <= 10⁴`
- `1 <= allowed.length <=26`
- `1 <= words[i].length <= 10`
- The characters in `allowed` are **distinct**.
- `words[i]` and `allowed` contain only lowercase English letters.

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
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            unique_chars = list(set(word))
            isConsistent = True
            for i in range(len(unique_chars)):
                if unique_chars[i] not in allowed:
                    isConsistent = False
            if isConsistent:
                count += 1
        return count

# @lc code=end

if __name__ == "__main__":
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    ans = Solution().countConsistentStrings(allowed, words)
    print("\noutput:", serialize(ans, "integer"))
