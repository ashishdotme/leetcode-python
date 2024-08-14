# Created by Ashish Patel at 2024/08/14 16:26
# leetgo: 1.4.7
# https://leetcode.com/problems/group-anagrams/

"""
49. Group Anagrams (Medium)
Given an array of strings `strs`, group **the anagrams** together. You can return the answer in
**any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

**Example 1:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**

```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**

```
Input: strs = ["a"]
Output: [["a"]]
```

**Constraints:**

- `1 <= strs.length <= 10⁴`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for s in strs:
            temp = []
            print(list(s))
            for t in strs[1:]:
                if sorted(list(s)) == sorted(list(t)):
                    temp.append(t)
            result.append(temp)
        return result
# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupAnagrams(strs)
    print("\noutput:", serialize(ans, "string[][]"))
