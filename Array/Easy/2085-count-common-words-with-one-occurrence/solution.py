# Created by Ashish Patel at 2025/01/16 00:06
# leetgo: 1.4.13
# https://leetcode.com/problems/count-common-words-with-one-occurrence/

"""
2085. Count Common Words With One Occurrence (Easy)
Given two string arrays `words1` and `words2`, return the number of strings that appear **exactly
once** in **each** of the two arrays.

**Example 1:**

```
Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not
count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
```

**Example 2:**

```
Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.
```

**Example 3:**

```
Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".
```

**Constraints:**

- `1 <= words1.length, words2.length <= 1000`
- `1 <= words1[i].length, words2[j].length <= 30`
- `words1[i]` and `words2[j]` consists only of lowercase English letters.

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
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        common_words =  list(set(words1) & set(words2))
        words1Counts = Counter(words1)
        words2Counts = Counter(words2)
        
        result = 0
        for word in common_words:
            if words1Counts[word] == 1 and words2Counts[word] == 1:
                result += 1
        return result
# @lc code=end

if __name__ == "__main__":
    words1 = ["a","ab"]
    words2 = ["a","a","a","ab"]
    ans = Solution().countWords(words1, words2)
    print("\noutput:", serialize(ans, "integer"))
