# Created by Ashish Patel at 2024/12/28 22:33
# leetgo: 1.4.13
# https://leetcode.com/problems/image-smoother/

"""
661. Image Smoother (Easy)
An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image
by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the
nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present,
we do not consider it in the average (i.e., the average of the four cells in the red smoother).

![](https://assets.leetcode.com/uploads/2021/05/03/smoother-grid.jpg)

Given an `m x n` integer matrix `img` representing the grayscale of an image, return the image after
applying the smoother on each cell of it.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/03/smooth-grid.jpg)

```
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/05/03/smooth2-grid.jpg)

```
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) =
141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
```

**Constraints:**

- `m == img.length`
- `n == img[i].length`
- `1 <= m, n <= 200`
- `0 <= img[i][j] <= 255`

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
import numpy as np
# @lc code=begin

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        ROWS = len(img)
        COLS = len(img[0])
        res = [[0] * COLS for _ in range(ROWS)]
        for row in range(len(img)):
            for col in range(len(img[0])):
                total = 0
                count = 0
                for i in range(row - 1, row + 2):
                    for j in range(col-1, col + 2):
                        if i < 0 or i == ROWS or j < 0 or j == COLS:
                            continue
                        total += img[i][j]
                        count += 1
                res[row][col] = total//count
        
        return res

# @lc code=end

if __name__ == "__main__":
    img = [[100,200,100],[200,50,200],[100,200,100]]
    ans = Solution().imageSmoother(img)
    print("\noutput:", serialize(ans, "integer[][]"))
