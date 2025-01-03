# Created by Ashish Patel at 2025/01/03 15:50
# leetgo: 1.4.11
# https://leetcode.com/problems/unique-morse-code-words/

"""
804. Unique Morse Code Words (Easy)
International Morse Code defines a standard encoding where each letter is mapped to a series of dots
and dashes, as follows:

- `'a'` maps to `".-"`,
- `'b'` maps to `"-..."`,
- `'c'` maps to `"-.-."`, and so on.

For convenience, the full table for the `26` letters of the English alphabet is given below:

```
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-
","...-",".--","-..-","-.--","--.."]
```

Given an array of strings `words` where each word can be written as a concatenation of the Morse
code of each letter.

- For example, `"cab"` can be written as `"-.-..--..."`, which is the concatenation of `"-.-."`, `".-"`, and
`"-..."`. We will call such a concatenation the **transformation** of a word.

Return the number of different **transformations** among all words we have.

**Example 1:**

```
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
```

**Example 2:**

```
Input: words = ["a"]
Output: 1
```

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 12`
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
import leetcode as lc

# @lc code=begin

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
            temp = []
            for ch in word:
                index = ord(ch)-ord('a')
                temp.append(codes[index])
            result.add(''.join(temp))
        return len(list(result))
# @lc code=end

if __name__ == "__main__":
    words: List[str] = ["gin","zen","gig","msg"]
    ans = Solution().uniqueMorseRepresentations(words)
    print("\noutput:", serialize(ans, "integer"))
