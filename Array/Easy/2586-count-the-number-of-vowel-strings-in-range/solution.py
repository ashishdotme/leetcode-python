# Created by Ashish Patel at 2025/01/08 16:37
# leetgo: 1.4.11
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

"""
2586. Count the Number of Vowel Strings in Range (Easy)
You are given a **0-indexed** array of string `words` and two integers `left` and `right`.

A string is called a **vowel string** if it starts with a vowel character and ends with a vowel
character where vowel characters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

Return the number of vowel strings  `words[i]` where  `i` belongs to the inclusive range  `[left,
right]`.

**Example 1:**

```
Input: words = ["are","amy","u"], left = 0, right = 2
Output: 2
Explanation:
- "are" is a vowel string because it starts with 'a' and ends with 'e'.
- "amy" is not a vowel string because it does not end with a vowel.
- "u" is a vowel string because it starts with 'u' and ends with 'u'.
The number of vowel strings in the mentioned range is 2.
```

**Example 2:**

```
Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
Output: 3
Explanation:
- "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
- "mu" is not a vowel string because it does not start with a vowel.
- "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
- "artro" is a vowel string because it starts with 'a' and ends with 'o'.
The number of vowel strings in the mentioned range is 3.
```

**Constraints:**

- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 10`
- `words[i]` consists of only lowercase English letters.
- `0 <= left <= right < words.length`

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
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        result = 0
        vowels = "aeiou"
        for i in range(left, right+1):
            word = words[i]
            first, last = word[0], word[-1]
            if first in vowels and last in vowels:
                result += 1
        return result

# @lc code=end

if __name__ == "__main__":
    words = ["are","amy","u"]
    left = 0
    right = 2
    ans = Solution().vowelStrings(words, left, right)
    print("\noutput:", serialize(ans, "integer"))
